# SendPulse REST API — Python SDK

Official Python client for the [SendPulse REST API](https://sendpulse.com/integrations/api).

- Python **≥ 3.11**, single runtime dependency (`httpx`)
- OAuth 2.0 and API key authentication with automatic token caching
- Services generated from OpenAPI specs; thin ergonomic layer on top
- mypy strict · ruff · 39 unit tests

## Installation

```bash
pip install pysendpulse
```

## Quick start

### API key auth

```python
from sendpulse import Client

client = Client(api_key="YOUR_API_KEY")
```

### OAuth (client credentials)

```python
client = Client(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")
```

Tokens are fetched automatically and stored on disk between requests.

## Services

| Method | Service |
|---|---|
| `client.email_service()` | Bulk email campaigns and mailing lists |
| `client.smtp_service()` | Transactional SMTP emails |
| `client.sms_service()` | SMS campaigns |
| `client.crm_service()` | CRM contacts and deals |
| `client.chatbot_service()` | Chatbot bots |

## Email service

```python
email = client.email_service()

# Campaigns
campaigns = email.campaigns().get_campaigns(limit=50)
campaign  = email.campaigns().get_campaign_by_id(123)

# Mailing lists
lists = email.mailing_lists().get_mailing_lists()
email.mailing_lists().create_mailing_list(body={"name": "My list"})
email.mailing_lists().update_mailing_list(456, body={"name": "Renamed"})
email.mailing_lists().delete_mailing_list(456)
```

## SMTP service

```python
smtp = client.smtp_service()

emails = smtp.emails().get_smtp_emails(limit=100, offset=0)
email  = smtp.emails().get_smtp_email_info("message-id")

smtp.emails().send_smtp_email(body={
    "email": {
        "html":    "<h1>Hello</h1>",
        "text":    "Hello",
        "subject": "Test",
        "from":    {"name": "Sender", "email": "sender@example.com"},
        "to":      [{"name": "Recipient", "email": "user@example.com"}],
    }
})
```

## SMS service

```python
sms = client.sms_service()

campaigns = sms.campaigns().get_sms_campaigns()
campaign  = sms.campaigns().get_sms_campaign_info(789)
```

## CRM service

```python
crm = client.crm_service()

# Contacts
contacts = crm.contacts().get_contacts_list()
contacts = crm.contacts().get_contact_list_by_email(body={"email": "alice@example.com"})
contact  = crm.contacts().get_contact_by_id(1)

# Deals
deals = crm.deals().get_deals_list()
deals = crm.deals().get_deals_list(body={"pipeline_id": 5})
deal  = crm.deals().get_deal(10)
```

## Chatbot service

```python
bots = client.chatbot_service().bots().get_bots()
```

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
    campaigns = client.email_service().campaigns().get_campaigns()
except AuthException as e:
    # check credentials
    print(e.http_status, e.raw_body)
except RateLimitException:
    # back off and retry
    pass
except ApiException as e:
    print(e.http_status, e.raw_body)
except ProtocolException as e:
    # unexpected response format
    print(e)
except NetworkException as e:
    # transport error
    print(e)
```

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
storage = InMemoryTokenStorage()

client = Client(
    client_id="id",
    client_secret="secret",
    token_storage=storage,
)
```

Default is `FileTokenStorage` (system temp directory or custom `cache_dir`).

## Context manager

Use `Client` as a context manager to ensure the underlying HTTP connection is released:

```python
with Client(api_key="YOUR_API_KEY") as client:
    lists = client.email_service().mailing_lists().get_mailing_lists()
```

## Documentation

| Document | Description |
|---|---|
| [CHANGELOG.md](CHANGELOG.md) | Release history |
| [docs/authentication.md](docs/authentication.md) | OAuth 2.0 and API key auth, token storage options |
| [docs/exceptions.md](docs/exceptions.md) | Exception hierarchy and error handling patterns |
| [docs/testing.md](docs/testing.md) | How to test your code using `FakeHttpClient` |
| [docs/fastapi.md](docs/fastapi.md) | FastAPI integration guide |

## License

MIT
