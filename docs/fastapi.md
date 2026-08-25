# FastAPI Integration

## Installation

```bash
pip install sendpulse-rest-api pydantic-settings
```

## Configuration

Create `config.py` using `pydantic-settings`:

```python
# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    sendpulse_client_id: str = ""
    sendpulse_client_secret: str = ""
    # or API key auth:
    # sendpulse_api_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
```

Add to `.env`:

```
SENDPULSE_CLIENT_ID=your-client-id
SENDPULSE_CLIENT_SECRET=your-client-secret
```

---

## Registering the Client

### Option 1 — lifespan singleton (recommended)

Create the client once at startup and share it for the lifetime of the application:

```python
# main.py
from contextlib import asynccontextmanager
from functools import lru_cache
from fastapi import FastAPI
from sendpulse import Client
from sendpulse.auth.token_storage import InMemoryTokenStorage
from config import Settings

@lru_cache
def get_settings() -> Settings:
    return Settings()

_sendpulse_client: Client | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global _sendpulse_client
    settings = get_settings()
    _sendpulse_client = Client(
        client_id=settings.sendpulse_client_id,
        client_secret=settings.sendpulse_client_secret,
        token_storage=InMemoryTokenStorage(),
    )
    yield
    _sendpulse_client = None

app = FastAPI(lifespan=lifespan)

def get_sendpulse() -> Client:
    assert _sendpulse_client is not None
    return _sendpulse_client
```

### Option 2 — `lru_cache` dependency

Simpler alternative; client is created on first request:

```python
from functools import lru_cache
from fastapi import Depends
from sendpulse import Client
from sendpulse.auth.token_storage import InMemoryTokenStorage
from config import Settings

@lru_cache
def get_settings() -> Settings:
    return Settings()

@lru_cache
def get_sendpulse(settings: Settings = Depends(get_settings)) -> Client:
    return Client(
        client_id=settings.sendpulse_client_id,
        client_secret=settings.sendpulse_client_secret,
        token_storage=InMemoryTokenStorage(),
    )
```

---

## Usage in routes

```python
from fastapi import APIRouter, Depends
from sendpulse import Client

router = APIRouter(prefix="/campaigns", tags=["campaigns"])

@router.get("/")
def list_campaigns(sendpulse: Client = Depends(get_sendpulse)):
    return sendpulse.email_service().campaigns().get_campaigns(limit=20)

@router.get("/{campaign_id}")
def get_campaign(campaign_id: int, sendpulse: Client = Depends(get_sendpulse)):
    return sendpulse.email_service().campaigns().get_campaign_by_id(campaign_id)
```

---

## Error Handling

Use FastAPI exception handlers to translate SDK exceptions into HTTP responses:

```python
from fastapi import Request
from fastapi.responses import JSONResponse
from sendpulse import AuthException, RateLimitException, ApiException, NetworkException, ProtocolException

@app.exception_handler(AuthException)
async def auth_exception_handler(request: Request, exc: AuthException):
    return JSONResponse(status_code=502, content={"detail": "SendPulse authentication failed"})

@app.exception_handler(RateLimitException)
async def rate_limit_handler(request: Request, exc: RateLimitException):
    return JSONResponse(status_code=429, content={"detail": "SendPulse rate limit exceeded"})

@app.exception_handler(ApiException)
async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(status_code=502, content={"detail": f"SendPulse API error: {exc.http_status}"})

@app.exception_handler(NetworkException)
@app.exception_handler(ProtocolException)
async def connection_error_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=502, content={"detail": "SendPulse connection error"})
```

---

## Background Tasks

For non-blocking sends use FastAPI's `BackgroundTasks`:

```python
from fastapi import BackgroundTasks, Depends
from sendpulse import Client

@router.post("/send-welcome")
def send_welcome(
    email: str,
    background_tasks: BackgroundTasks,
    sendpulse: Client = Depends(get_sendpulse),
):
    def _send():
        sendpulse.smtp_service().emails().send_smtp_email({
            "email": {
                "html":    "<h1>Welcome!</h1>",
                "subject": "Welcome to our service",
                "from":    {"name": "App", "email": "no-reply@example.com"},
                "to":      [{"email": email}],
            }
        })

    background_tasks.add_task(_send)
    return {"status": "queued"}
```

For high-volume or retry-capable sends, use **Celery**:

```python
# tasks.py
from celery import Celery
from sendpulse import Client
from config import Settings

celery = Celery("tasks", broker="redis://localhost:6379/0")
settings = Settings()
_client = Client(
    client_id=settings.sendpulse_client_id,
    client_secret=settings.sendpulse_client_secret,
)

@celery.task(autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def send_email(payload: dict) -> None:
    _client.smtp_service().emails().send_smtp_email(payload)
```

```python
# in your route
from tasks import send_email

send_email.delay(payload)
```

---

## Testing

Override the `get_sendpulse` dependency in tests using `app.dependency_overrides`:

```python
# test_campaigns.py
import pytest
from fastapi.testclient import TestClient
from sendpulse import Client
from main import app, get_sendpulse

class FakeHttpClient:
    def __init__(self, *responses):
        from collections import deque
        self._queue = deque(responses)
    def send(self, request):
        return self._queue.popleft()

def make_fake_client(responses):
    from sendpulse.http.response import Response
    fake_http = FakeHttpClient(*responses)
    return Client(api_key="test", http_client=fake_http)

@pytest.fixture
def test_client():
    return TestClient(app)

def test_list_campaigns_returns_data(test_client):
    from sendpulse.http.response import Response

    fake_sp = make_fake_client([
        Response(200, {}, '[{"id": 1, "name": "Promo"}]')
    ])
    app.dependency_overrides[get_sendpulse] = lambda: fake_sp

    response = test_client.get("/campaigns/")

    assert response.status_code == 200
    assert response.json()[0]["name"] == "Promo"

    app.dependency_overrides.clear()
```
