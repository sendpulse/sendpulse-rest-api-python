# Authentication

The SDK supports two authentication methods: **OAuth 2.0** (recommended) and **API key**.

## OAuth 2.0 (client credentials)

```python
from sendpulse import Client

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

## API Key

```python
client = Client(api_key="YOUR_API_KEY")
```

- Simpler setup, no token management
- The key is sent as a `Bearer` header on every request
- Does not support automatic refresh — if the key is revoked, requests fail with `AuthException`

Use API key auth for quick scripts or environments where OAuth token caching is not practical.

---

## Token Storage

Token storage only applies to OAuth. The SDK ships with two implementations.

### FileTokenStorage (default)

Tokens are stored as JSON files in a per-user subdirectory of the system temp directory (e.g. `/tmp/sendpulse-1000-tokens`), or in a custom path. Suitable for single-server setups.

```python
# default — uses tempfile.gettempdir()
client = Client(client_id="...", client_secret="...")

# custom directory
client = Client(
    client_id="...",
    client_secret="...",
    cache_dir="/var/cache/myapp",
)
```

Files are written atomically (temp file + replace).

### InMemoryTokenStorage

Stores the token in memory for the duration of the process. Suitable for CLI scripts and tests.

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
| Multiple servers / containers | Custom storage backed by Redis (see below) |
| CLI script / one-off job | `InMemoryTokenStorage` |
| Tests | `InMemoryTokenStorage` |
| FastAPI | `InMemoryTokenStorage` or custom (see [fastapi.md](fastapi.md)) |

---

## Custom TokenStorage

Implement the `TokenStorage` protocol to use any backend:

```python
from sendpulse.auth.token_storage import TokenData
from sendpulse.auth.protocol import TokenStorageProtocol

class RedisTokenStorage(TokenStorageProtocol):
    def __init__(self, redis_client):
        self._redis = redis_client

    def get(self, key: str) -> TokenData | None:
        raw = self._redis.get(f"sendpulse:{key}")
        if raw is None:
            return None
        import json
        data = json.loads(raw)
        return TokenData(
            access_token=data["access_token"],
            token_type=data["token_type"],
            expires_at=data["expires_at"],
        )

    def set(self, key: str, token: TokenData) -> None:
        import json, time
        ttl = max(0, token["expires_at"] - int(time.time()))
        self._redis.setex(
            f"sendpulse:{key}",
            ttl,
            json.dumps({
                "access_token": token["access_token"],
                "token_type":   token["token_type"],
                "expires_at":   token["expires_at"],
            }),
        )

    def delete(self, key: str) -> None:
        self._redis.delete(f"sendpulse:{key}")

client = Client(
    client_id="...",
    client_secret="...",
    token_storage=RedisTokenStorage(redis_client),
)
```

The `TokenData` object passed to `set()` is a `TypedDict` with this shape:

```python
token["access_token"]  # str
token["token_type"]    # str  — always "Bearer"
token["expires_at"]    # int  — Unix timestamp
```
