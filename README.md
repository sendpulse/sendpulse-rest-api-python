# SendPulse REST API — Python SDK

Official Python client for the [SendPulse REST API](https://sendpulse.com/integrations/api).

- Python **≥ 3.11**, single runtime dependency (`httpx`)
- Thin transport: OAuth / API-key auth, automatic token refresh, typed exceptions
- **Chained endpoint surface** with IDE autocomplete — `client.crm.deals.getDeal({...})`
- Raw `get/post/...` fallback for any endpoint
- Swappable HTTP client and token storage
- Ships `llms.txt` for AI coding assistants · mypy strict · ruff

## Installation

```bash
pip install pysendpulse
```

```python
from sendpulse import Client
```

## Quick start

### API key auth

```python
client = Client(api_key="YOUR_API_KEY")
```

### OAuth (client credentials)

```python
client = Client(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")
```

Tokens are fetched automatically and stored on disk between requests. A `401` is
retried once with a freshly minted token.

## Calling endpoints

### Chained surface

Mapped endpoints are reachable as a chain — `service → resource → operation` —
with IDE autocomplete for every segment:

```python
campaigns = client.email.campaigns.getCampaigns({"limit": 10})
campaign  = client.email.campaigns.getCampaignById({"id": 12345})

deal = client.crm.deals.getDeal({"dealId": 42})

client.smtp.emails.sendSmtpEmail({
    "email": {
        "subject": "Hello",
        "from": {"name": "Me", "email": "me@example.com"},
        "to": [{"name": "You", "email": "you@example.com"}],
        "html": "<p>Hi!</p>",
    },
})
```

You pass **one dict**. Path params (`{id}`) and declared query params are routed
automatically; **any other key goes to the JSON body** (for a `GET` it becomes a
query param). Every call returns the decoded JSON response (a `dict` or `list`;
empty body → `{}`), or raises one of the exceptions below.

> **Hyphenated services** (`file-manager`, `live-chat`, `viber-chatbot`,
> `web-push`) are not valid attribute names — reach them via `getattr`:
> `getattr(client, "file-manager").directory.getDirectoryTree({})`.

The full list of chains, paths and parameters lives in
[`sendpulse/resources/operations/`](sendpulse/resources/operations) and is
mirrored in [`llms.txt`](llms.txt).

### Raw requests

For any endpoint not in the map — or when you want full control — call a path
directly:

```python
client.get("/campaigns", {"limit": 10})            # also query params
client.post("/smtp/emails", {"email": {}})          # put / patch / delete too

# lowest level:
client.request("GET", "/campaigns")
from sendpulse.http.request import Request
client.send(Request(method="GET", uri="/campaigns"))
```

## IDE autocomplete

The chained surface is powered by generated stub definitions in
[`sendpulse/stubs.pyi`](sendpulse/stubs.pyi):

- **PyCharm / VS Code (Pylance)** index the `.pyi` automatically — no setup.
- **mypy** resolves the chain and flags unknown resources/methods and missing
  required params. Each operation's HTTP route and parameter list is in its
  docstring (shown on hover).

## Error handling

```python
from sendpulse import (
    Client,
    AuthException,       # 401 / 403 — wrong credentials or insufficient permissions
    RateLimitException,  # 429 — too many requests
    ApiException,        # any other 4xx / 5xx from the API
    NetworkException,    # connection timeout, DNS failure, etc.
    ProtocolException,   # response received but could not be parsed (malformed JSON)
)

try:
    campaigns = client.email.campaigns.getCampaigns()
except AuthException as e:
    print(e.http_status, e.raw_body)   # 401 / 403 — credentials problem
except RateLimitException:
    ...                                # 429 — back off and retry
except ApiException as e:
    print(e.http_status, e.raw_body)   # other 4xx / 5xx
except ProtocolException as e:
    ...                                # unexpected response format
except NetworkException as e:
    ...                                # transport error
```

All SDK exceptions subclass `sendpulse.SendPulseError`, so a single
`except SendPulseError` covers every SDK error.

## Configuration

```python
client = Client(
    api_key="key",
    connect_timeout=10.0,   # seconds, default
    request_timeout=30.0,   # seconds, default
)
```

## Custom HTTP client

Any object that implements `send(request: Request) -> Response` is accepted:

```python
from sendpulse.http.request import Request
from sendpulse.http.response import Response

class MyHttpClient:
    def send(self, request: Request) -> Response:
        ...

client = Client(api_key="key", http_client=MyHttpClient())
```

## Custom token storage

```python
from sendpulse.auth.token_storage import InMemoryTokenStorage

# In-memory (tokens lost on process exit — useful for tests)
client = Client(
    client_id="id",
    client_secret="secret",
    token_storage=InMemoryTokenStorage(),
)
```

Default is `FileTokenStorage` (system temp directory or custom `cache_dir`).

## Context manager

Use `Client` as a context manager to release the underlying HTTP connection:

```python
with Client(api_key="YOUR_API_KEY") as client:
    lists = client.email.mailingLists.getMailingLists()
```

## Documentation

| Topic | |
|---|---|
| Authentication & token storage | [docs/authentication.md](docs/authentication.md) |
| Exception reference | [docs/exceptions.md](docs/exceptions.md) |
| Testing | [docs/testing.md](docs/testing.md) |
| FastAPI integration | [docs/fastapi.md](docs/fastapi.md) |
| Architecture & decisions | [docs/architecture.md](docs/architecture.md) |
| AI assistants | [llms.txt](llms.txt) |

## License

MIT
