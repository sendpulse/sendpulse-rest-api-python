from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Bot:
    id: str | None = None
    channel_data: dict[str, Any] | None = None
    inbox: dict[str, Any] | None = None
    status: int | None = None
    created_at: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Bot:
        return cls(
            id=data.get("id"),
            channel_data=data.get("channel_data"),
            inbox=data.get("inbox"),
            status=data.get("status"),
            created_at=data.get("created_at"),
        )
