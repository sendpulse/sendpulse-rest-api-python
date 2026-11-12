# Exception reference

All SDK exceptions subclass `sendpulse.SendPulseError` and are raised only — never swallowed internally.

## Hierarchy

```
sendpulse.SendPulseError                     (base — catch-all for the SDK)
├── SendPulseException                        (API-level; carries status + body)
│   ├── AuthException        — 401 / 403
│   ├── RateLimitException   — 429
│   └── ApiException         — other 4xx / 5xx
├── NetworkException         — transport failure (timeout, DNS, refused)
└── ProtocolException        — response received but cannot be parsed
```

`SendPulseException` (and its subclasses) carry two attributes:

```python
e.http_status   # int  — HTTP status code
e.raw_body      # str  — raw response body
```

`NetworkException` and `ProtocolException` do not have these — they occur before or outside of a valid HTTP exchange.

> Note: unlike some SDKs there is no separate `ForbiddenException`; a `403` is
> reported as `AuthException` (check `e.http_status` to distinguish `401` from `403`).

---

## AuthException

**When:** API returns `401` or `403`.

**Causes:**
- Invalid or expired API key
- Invalid OAuth credentials (`client_id` / `client_secret`)
- `403`: current tariff plan or account permissions do not allow the request

**What to do:** check your credentials and subscription. For OAuth, the SDK
automatically retries once with a fresh token on `401` before raising — so if you
see this exception, the refresh also failed. A `403` will not be helped by retrying.

```python
except AuthException as e:
    print(e.http_status)   # 401 or 403
    print(e.raw_body)      # {"error": "..."}
```

---

## RateLimitException

**When:** API returns `429`.

**Causes:** exceeded the request rate limit (SendPulse allows up to 10 requests per second).

**What to do:** back off and retry. Consider queuing high-volume operations.

```python
except RateLimitException:
    time.sleep(1)
    # retry or dispatch to a queue
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
    print(e.http_status)   # e.g. 422
    print(e.raw_body)      # {"message": "The email field is required."}
```

---

## NetworkException

**When:** the HTTP request could not be completed at the transport level (DNS
failure, connection refused or timed out, TLS error).

No HTTP response was received. Retrying after a delay is often appropriate.

```python
except NetworkException as e:
    print(e)   # underlying httpx transport error
```

---

## ProtocolException

**When:** a response was received but could not be parsed (malformed JSON from the
API, or an unexpected OAuth token response shape).

Unlike `NetworkException`, the network itself worked. Retrying is unlikely to help until the API-side issue is resolved.

```python
except ProtocolException as e:
    print(e)   # "Failed to decode response body: ..."
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
    result = client.smtp.emails.sendSmtpEmail(payload)
except AuthException:
    ...          # 401 / 403 — credentials or permissions, do not retry
except RateLimitException:
    ...          # 429 — slow down, retry after delay
except ApiException as e:
    ...          # other 4xx / 5xx — log and inspect e.raw_body
except ProtocolException:
    ...          # unexpected response format — log and alert
except NetworkException:
    ...          # transport failure — retry after delay
```

To catch any SDK exception in one block:

```python
from sendpulse import SendPulseError

try:
    ...
except SendPulseError as e:
    log_error(str(e))
```
