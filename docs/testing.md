# Testing

## Testing your own code that uses the SDK

The recommended approach is to **not mock `Client`** — instead, substitute the HTTP
transport with a fake. Your tests then exercise real SDK logic (request building,
auth, response parsing, dispatch) without making network calls.

### FakeHttpClient

The test suite ships `FakeHttpClient` in `tests/fixture/`. It implements the
`HttpClient` protocol and lets you queue pre-built responses:

```python
from sendpulse.http.response import Response
from tests.fixture.fake_http_client import FakeHttpClient

fake = FakeHttpClient()
fake.queue(Response(200, {}, json.dumps([
    {"id": 1, "name": "Newsletter"},
    {"id": 2, "name": "Promo"},
])))
```

Pass it to `Client` via the `http_client` argument:

```python
from sendpulse import Client

client = Client(api_key="test-key", http_client=fake)
```

Now `client` makes no real HTTP calls — every request returns the next queued response.

### Full example

```python
import json

from sendpulse import Client
from sendpulse.http.response import Response
from tests.fixture.fake_http_client import FakeHttpClient


def test_get_campaigns_returns_decoded_list() -> None:
    http = FakeHttpClient()
    http.queue(Response(200, {}, json.dumps([{"id": 42, "name": "Black Friday"}])))
    client = Client(api_key="test", http_client=http)

    campaigns = client.email.campaigns.getCampaigns()

    assert campaigns == [{"id": 42, "name": "Black Friday"}]


def test_get_campaigns_builds_correct_request() -> None:
    http = FakeHttpClient()
    http.queue(Response(200, {}, "[]"))
    client = Client(api_key="test", http_client=http)

    client.email.campaigns.getCampaigns({"limit": 50, "offset": 10})

    req = http.last_request()
    assert req.params == {"limit": 50, "offset": 10}
```

### FakeHttpClient API

| Method | Description |
|---|---|
| `queue(*responses)` | Enqueue one or more responses to return in order |
| `last_request()` | Returns the most recently sent request |
| `all_requests()` | Returns all requests sent so far |
| `call_count()` | Number of HTTP calls made |

---

## Testing error handling

Queue an error response to verify your `except` blocks:

```python
import pytest

from sendpulse import AuthException, RateLimitException
from sendpulse.http.response import Response


def test_handles_auth_error() -> None:
    http = FakeHttpClient()
    http.queue(Response(401, {}, '{"error": "Unauthorized"}'))
    client = Client(api_key="test", http_client=http)

    with pytest.raises(AuthException):
        client.email.campaigns.getCampaigns()


def test_handles_rate_limit() -> None:
    http = FakeHttpClient()
    http.queue(Response(429, {}, '{"error": "Too Many Requests"}'))
    client = Client(api_key="test", http_client=http)

    with pytest.raises(RateLimitException):
        client.smtp.emails.sendSmtpEmail({})
```

---

## Token storage in tests

Use `InMemoryTokenStorage` to avoid file I/O and keep tests isolated:

```python
from sendpulse.auth.token_storage import InMemoryTokenStorage

client = Client(
    client_id="test-id",
    client_secret="test-secret",
    http_client=fake,
    token_storage=InMemoryTokenStorage(),
)
```

---

## Running the SDK's own test suite

```bash
pip install -e ".[dev]"
pytest
mypy sendpulse tests
ruff check sendpulse tests
```
