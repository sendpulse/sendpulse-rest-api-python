# Authentication

The SDK supports two authentication methods: **OAuth 2.0** (recommended) and **API key**.

## OAuth 2.0 (client credentials)

```python
client = Client(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
```

- Tokens are fetched automatically on the first request
- Cached and reused until 5 minutes before expiry
- On a `401` response the SDK invalidates the token, fetches a new one, and retries once
- You never handle tokens manually

Obtain `client_id` and `client_secret` from your [SendPulse API settings](https://sendpulse.com/settings/api).

## API key

```python
client = Client(api_key="YOUR_API_KEY")
```

- Simpler setup, no token management
- The key is sent as a `Bearer` header on every request
- Does not support automatic refresh — if the key is revoked, requests fail with `AuthException`

Use API key auth for quick scripts or environments where OAuth token caching is not practical.

---

## Token storage

Token storage only applies to OAuth. The SDK ships with two implementations.

### FileTokenStorage (default)

Tokens are stored as JSON files in the system temp directory (or a custom path). Suitable for single-server setups.

```python
# default — uses the system temp directory
client = Client(client_id="...", client_secret="...")

# custom directory
client = Client(
    client_id="...",
    client_secret="...",
    cache_dir="/var/cache/myapp",
)
```

Files are written atomically (temp file + rename) with exclusive locking (where
`fcntl` is available) and `0600` permissions.

### InMemoryTokenStorage

Stores the token in memory for the duration of the process. Suitable for CLI scripts and tests where persistence between requests is not needed.

```python
from sendpulse.auth.token_storage import InMemoryTokenStorage

client = Client(
    client_id="...",
    client_secret="...",
    token_storage=InMemoryTokenStorage(),
)
```

---

## Choosing a storage

| Environment | Recommended storage |
|---|---|
| Single server, long-running process | `FileTokenStorage` |
| Multiple servers / containers | custom storage backed by a shared cache (see below) |
| CLI script / one-off job | `InMemoryTokenStorage` |
| Tests | `InMemoryTokenStorage` |

---

## Custom token storage

Any object implementing the three-method storage protocol is accepted — e.g. to
back tokens with Redis so they are shared across processes and servers:

```python
import json

import redis

from sendpulse.auth.token_storage import TokenData


class RedisTokenStorage:
    def __init__(self, client: redis.Redis) -> None:
        self._redis = client

    def get(self, key: str) -> TokenData | None:
        raw = self._redis.get(f"sp_token:{key}")
        return json.loads(raw) if raw else None

    def set(self, key: str, token: TokenData) -> None:
        self._redis.set(f"sp_token:{key}", json.dumps(token))

    def delete(self, key: str) -> None:
        self._redis.delete(f"sp_token:{key}")


client = Client(
    client_id="...",
    client_secret="...",
    token_storage=RedisTokenStorage(redis.Redis()),
)
```

The `token` dict passed to `set()` always has this shape:

```python
{
    "access_token": str,
    "token_type": str,   # always "Bearer"
    "expires_at": int,   # Unix timestamp
}
```
