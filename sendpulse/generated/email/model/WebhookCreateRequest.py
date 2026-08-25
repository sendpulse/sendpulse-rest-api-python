from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class WebhookCreateRequest:
    url: str | None = None
    actions: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WebhookCreateRequest:
        return cls(
            url=data.get("url"),
            actions=data.get("actions"),
        )
