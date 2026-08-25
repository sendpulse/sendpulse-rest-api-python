from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.email.model.Webhook import Webhook


@dataclass(slots=True)
class WebhookResponse:
    success: bool | None = None
    data: Webhook | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WebhookResponse:
        return cls(
            success=data.get("success"),
            data=Webhook.from_dict(data["data"]) if isinstance(data.get("data"), dict) else None,
        )
