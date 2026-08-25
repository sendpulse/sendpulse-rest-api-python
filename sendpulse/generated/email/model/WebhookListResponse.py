from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.email.model.Webhook import Webhook


@dataclass(slots=True)
class WebhookListResponse:
    success: bool | None = None
    data: list[Webhook] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WebhookListResponse:
        return cls(
            success=data.get("success"),
            data=[Webhook.from_dict(i) for i in data["data"]] if isinstance(data.get("data"), list) else None,
        )
