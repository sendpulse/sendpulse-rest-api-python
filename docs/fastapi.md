# FastAPI integration

The SDK `Client` is **synchronous** (it uses `httpx.Client`). In an async FastAPI
app, run SDK calls so they don't block the event loop — either declare the
endpoint with `def` (FastAPI runs sync endpoints in a threadpool) or wrap calls
in `run_in_threadpool`.

## Provide a single Client as a dependency

Create one `Client` for the app lifetime and inject it:

```python
from collections.abc import Iterator
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException

from sendpulse import ApiException, AuthException, Client, RateLimitException


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.sp = Client(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    yield
    app.state.sp.close()


app = FastAPI(lifespan=lifespan)


def get_client() -> Client:
    return app.state.sp
```

## Sync endpoint (offloaded to a threadpool)

Declaring the handler with `def` (not `async def`) lets FastAPI run it in a
threadpool, so the blocking SDK call is safe:

```python
@app.get("/campaigns")
def list_campaigns(client: Client = Depends(get_client)):
    return client.email.campaigns.getCampaigns({"limit": 50})
```

## Async endpoint

If the handler must be `async def`, offload the blocking call:

```python
from fastapi.concurrency import run_in_threadpool


@app.get("/deals/{deal_id}")
async def get_deal(deal_id: int, client: Client = Depends(get_client)):
    return await run_in_threadpool(client.crm.deals.getDeal, {"dealId": deal_id})
```

## Map SDK exceptions to HTTP responses

A small exception handler translates SDK errors into clean HTTP responses:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

from sendpulse import ApiException, AuthException, RateLimitException, SendPulseError


@app.exception_handler(SendPulseError)
async def sendpulse_error_handler(request: Request, exc: SendPulseError):
    if isinstance(exc, AuthException):
        return JSONResponse(status_code=502, content={"detail": "SendPulse auth failed"})
    if isinstance(exc, RateLimitException):
        return JSONResponse(status_code=429, content={"detail": "Rate limited, retry later"})
    if isinstance(exc, ApiException):
        return JSONResponse(status_code=502, content={"detail": exc.raw_body})
    return JSONResponse(status_code=502, content={"detail": "SendPulse request failed"})
```

## Multi-worker token storage

Under multiple workers, back OAuth tokens with a shared store instead of the
default per-process file cache — see
[authentication.md](authentication.md#custom-token-storage) for a Redis example.
