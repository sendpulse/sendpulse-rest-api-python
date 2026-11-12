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

# ── OAuth (recommended for production) ────────────────────────────────────────
client = Client(
    client_id=os.environ.get("SENDPULSE_CLIENT_ID", "your-client-id"),
    client_secret=os.environ.get("SENDPULSE_CLIENT_SECRET", "your-client-secret"),
)

# ── or a static API key ───────────────────────────────────────────────────────
# client = Client(api_key=os.environ.get("SENDPULSE_API_KEY", "your-api-key"))

# ── or with custom token cache and timeouts ───────────────────────────────────
# client = Client(
#     client_id="your-client-id",
#     client_secret="your-client-secret",
#     cache_dir="/var/cache/sendpulse",
#     connect_timeout=5.0,
#     request_timeout=15.0,
# )

try:
    # ── Chained surface: service → resource → operation, one dict argument ─────
    campaigns = client.email.campaigns.getCampaigns({"limit": 10})

    print(f"Campaigns ({len(campaigns)}):")
    for campaign in campaigns:
        print(f"  [{campaign['id']}] {campaign['name']}")

    # Single campaign by id
    # campaign = client.email.campaigns.getCampaignById({"id": 12345})

    # Send a transactional email
    # client.smtp.emails.sendSmtpEmail({
    #     "email": {
    #         "subject": "Hello",
    #         "from": {"name": "Me", "email": "me@example.com"},
    #         "to": [{"name": "You", "email": "you@example.com"}],
    #         "html": "<p>Hi!</p>",
    #     },
    # })

    # ── Raw request: any path not in the map ──────────────────────────────────
    # senders = client.get("/senders")

    # Hyphenated services (file-manager, live-chat, viber-chatbot, web-push) are
    # not valid attribute names — reach them via getattr:
    #   getattr(client, "file-manager").directory.getDirectoryTree({})

except AuthException as e:
    # 401 / 403 — invalid key or token, or insufficient permissions
    print(f"Auth error {e.http_status}: {e.raw_body}")
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
    # transport error / timeout
    print(f"Network error: {e}")
    sys.exit(1)
