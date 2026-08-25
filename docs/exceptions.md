# Exception Reference

All SDK exceptions inherit from `Exception` and are thrown only — never swallowed internally.

## Hierarchy

```
Exception
├── SendPulseException
│   ├── AuthException       — 401, 403
│   ├── RateLimitException  — 429
│   └── ApiException        — other 4xx, 5xx
├── NetworkException        — transport / httpx failure
└── ProtocolException       — response received but cannot be parsed
```

`SendPulseException` carries two attributes:

```python
e.http_status  # int    — HTTP status code
e.raw_body     # str    — raw response body
```

`NetworkException` and `ProtocolException` do not have these — they occur before or outside of a valid HTTP exchange.

---

## AuthException

**When:** API returns `401` or `403`.

**Causes:**
- Invalid or expired API key
- Invalid OAuth credentials (`client_id` / `client_secret`)
- Insufficient permissions for the requested resource

**What to do:** check your credentials. For OAuth, the SDK automatically retries once with a fresh token on `401` before throwing — so if you see this exception, the refresh also failed.

```python
except AuthException as e:
    print(e.http_status)  # 401 or 403
    print(e.raw_body)     # {"error": "..."}
```

---

## RateLimitException

**When:** API returns `429`.

**Causes:** exceeded the request rate limit (SendPulse allows up to 10 requests per second).

**What to do:** back off and retry. Consider queuing high-volume operations.

```python
except RateLimitException:
    time.sleep(1)
    # retry or dispatch to queue
```

---

## ApiException

**When:** API returns any other `4xx` or `5xx` response.

**Causes:**
- `400` — malformed request body
- `404` — resource not found
- `422` — validation error
- `500` — internal server error on SendPulse side

```python
except ApiException as e:
    print(e.http_status)  # e.g. 422
    print(e.raw_body)     # {"message": "The email field is required."}
```

---

## NetworkException

**When:** the HTTP request could not be completed at the transport level.

**Causes:**
- DNS resolution failure
- Connection refused or timed out
- SSL/TLS handshake error
- httpx transport error

No HTTP response was received. Retrying after a delay is often appropriate.

```python
except NetworkException as e:
    print(e)  # "Connection error: ..."
```

---

## ProtocolException

**When:** a response was received but could not be parsed.

**Causes:**
- API returned malformed JSON (e.g. during a server-side incident)
- OAuth token endpoint returned an unexpected response shape

Unlike `NetworkException`, the network itself worked. Retrying is unlikely to help until the API-side issue is resolved.

```python
except ProtocolException as e:
    print(e)  # "Failed to decode response body: ..."
```

---

## Recommended catch order

Catch from most specific to least specific:

```python
from sendpulse import (
    AuthException,
    RateLimitException,
    ApiException,
    ProtocolException,
    NetworkException,
)

try:
    result = client.smtp_service().emails().send_smtp_email(payload)
except AuthException as e:
    # credentials problem — do not retry
    pass
except RateLimitException:
    # slow down — retry after delay
    pass
except ApiException as e:
    # API rejected the request — log and inspect e.raw_body
    pass
except ProtocolException as e:
    # unexpected response format — log and alert
    pass
except NetworkException as e:
    # transport failure — retry after delay
    pass
```

To catch any HTTP-level SDK exception in one block:

```python
from sendpulse import SendPulseException

try:
    # ...
    pass
except SendPulseException as e:
    # covers AuthException, RateLimitException, ApiException
    print(e.http_status, e.raw_body)
except Exception as e:
    # covers NetworkException and ProtocolException
    print(e)
```
