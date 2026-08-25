from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class WebhookUpdateRequest:
    url: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WebhookUpdateRequest:
        return cls(
            url=data.get("url"),
        )
