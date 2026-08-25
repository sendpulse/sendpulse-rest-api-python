"""SendPulse Python SDK — quickstart example."""

import os
import sys

from sendpulse import (
    ApiException,
    AuthException,
    Client,
    NetworkException,
    RateLimitException,
)

# ── OAuth (recommended for production) ───────────────────────────────────────
client = Client(
    client_id=os.environ.get("SENDPULSE_CLIENT_ID", "your-client-id"),
    client_secret=os.environ.get("SENDPULSE_CLIENT_SECRET", "your-client-secret"),
)

# ── or a static API key ───────────────────────────────────────────────────────
# client = Client(api_key=os.environ.get("SENDPULSE_API_KEY", "your-api-key"))

# ── with custom token cache and timeouts ──────────────────────────────────────
# client = Client(
#     client_id="your-client-id",
#     client_secret="your-client-secret",
#     cache_dir="/var/cache/sendpulse",
#     connect_timeout=5.0,
#     request_timeout=15.0,
# )

# ── list campaigns ────────────────────────────────────────────────────────────
try:
    campaigns = client.email_service().campaigns().get_campaigns(limit=10)

    print(f"Campaigns ({len(campaigns)}):")
    for campaign in campaigns:
        print(f"  [{campaign.id}] {campaign.name}")

except AuthException as e:
    # 401 or 403 — invalid key or token
    print(f"Auth error: {e}")
    sys.exit(1)
except RateLimitException:
    # 429 — request rate limit exceeded (10 req/s)
    print("Rate limited — slow down")
    sys.exit(1)
except ApiException as e:
    # other 4xx / 5xx
    print(f"API error {e.http_status}: {e.raw_body}")
    sys.exit(1)
except NetworkException as e:
    # network error, timeout, or invalid JSON in response
    print(f"Network error: {e}")
    sys.exit(1)

# ── fetch a single campaign by ID ─────────────────────────────────────────────
# campaign = client.email_service().campaigns().get_campaign_by_id(12345)
# print(campaign.name)
