from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Webhook:
    id: int | None = None
    user_id: int | None = None
    url: str | None = None
    action: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Webhook:
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            url=data.get("url"),
            action=data.get("action"),
        )
