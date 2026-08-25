# Testing

## Testing your own code that uses the SDK

The recommended approach is to **not mock `Client` at all** — instead, substitute the HTTP transport layer with a fake. This way your tests exercise real SDK logic (request building, response parsing, model hydration) without making network calls.

### FakeHttpClient

Create a simple fake that implements the same interface as the SDK's HTTP client:

```python
from dataclasses import dataclass, field
from sendpulse.http.request import Request
from sendpulse.http.response import Response


@dataclass
class FakeHttpClient:
    responses: list[Response] = field(default_factory=list)
    calls: list[Request] = field(default_factory=list)
    _index: int = field(default=0, init=False)

    def send(self, request: Request) -> Response:
        self.calls.append(request)
        response = self.responses[self._index]
        self._index += 1
        return response

    @property
    def call_count(self) -> int:
        return self._index

    @staticmethod
    def ok(body: str = '{"ok": true}') -> Response:
        return Response(status_code=200, headers={}, body=body)

    @staticmethod
    def error(status: int, body: str = "error") -> Response:
        return Response(status_code=status, headers={}, body=body)
```

Pass it to `Client` via the `http_client` argument:

```python
from sendpulse import Client
from sendpulse.auth.token_storage import InMemoryTokenStorage

fake = FakeHttpClient(responses=[FakeHttpClient.ok('[{"id": 1, "name": "Newsletter"}]')])

client = Client(api_key="test-key", http_client=fake)
```

Now `client` makes no real HTTP calls — every `send()` returns the next queued response.

---

### pytest fixture

```python
# conftest.py
import pytest
from sendpulse import Client
from sendpulse.auth.token_storage import InMemoryTokenStorage


@pytest.fixture
def fake_http():
    return FakeHttpClient()


@pytest.fixture
def sendpulse_client(fake_http):
    return Client(api_key="test-key", http_client=fake_http), fake_http
```

### Full example

```python
def test_get_campaigns_returns_mapped_models(sendpulse_client):
    client, fake = sendpulse_client
    fake.responses.append(FakeHttpClient.ok('[{"id": 42, "name": "Black Friday"}]'))

    campaigns = client.email_service().campaigns().get_campaigns()

    assert len(campaigns) == 1
    assert campaigns[0].id == 42
    assert campaigns[0].name == "Black Friday"


def test_get_campaigns_builds_correct_request(sendpulse_client):
    client, fake = sendpulse_client
    fake.responses.append(FakeHttpClient.ok("[]"))

    client.email_service().campaigns().get_campaigns(limit=50, offset=10)

    req = fake.calls[-1]
    assert "limit=50" in req.uri
    assert "offset=10" in req.uri
```

---

## Testing error handling

Queue an error response to verify your exception handling:

```python
from sendpulse import AuthException, RateLimitException
import pytest


def test_handles_auth_error(sendpulse_client):
    client, fake = sendpulse_client
    fake.responses.append(FakeHttpClient.error(401, '{"error": "Unauthorized"}'))

    with pytest.raises(AuthException):
        client.email_service().campaigns().get_campaigns()


def test_handles_rate_limit(sendpulse_client):
    client, fake = sendpulse_client
    fake.responses.append(FakeHttpClient.error(429, '{"error": "Too Many Requests"}'))

    with pytest.raises(RateLimitException):
        client.smtp_service().emails().send_smtp_email({})
```

---

## Token storage in tests

Use `InMemoryTokenStorage` to avoid file I/O and keep tests isolated:

```python
from sendpulse import Client
from sendpulse.auth.token_storage import InMemoryTokenStorage

token_resp = '{"access_token": "tok", "token_type": "Bearer", "expires_in": 3600}'

fake = FakeHttpClient(responses=[
    FakeHttpClient.ok(token_resp),   # token fetch
    FakeHttpClient.ok('{"id": 1}'),  # actual API call
])

client = Client(
    client_id="test-id",
    client_secret="test-secret",
    http_client=fake,
    token_storage=InMemoryTokenStorage(),
)
```

---

## Testing code that wraps the SDK

If you inject `Client` into your own services, type-hint against it and override in tests:

```python
# my_service.py
from sendpulse import Client

class EmailNotifier:
    def __init__(self, sendpulse: Client) -> None:
        self._sp = sendpulse

    def notify(self, to: str, subject: str, html: str) -> None:
        self._sp.smtp_service().emails().send_smtp_email({
            "email": {
                "html": html, "subject": subject,
                "from": {"name": "App", "email": "no-reply@example.com"},
                "to":   [{"email": to}],
            }
        })


# test_my_service.py
def test_notify_sends_email():
    fake = FakeHttpClient(responses=[FakeHttpClient.ok()])
    client = Client(api_key="test", http_client=fake)
    notifier = EmailNotifier(sendpulse=client)

    notifier.notify("user@example.com", "Hello", "<p>Hi</p>")

    assert fake.call_count == 1
    assert "smtp" in fake.calls[0].uri
```
