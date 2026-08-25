from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DealHistory:
    id: int | None = None
    userId: int | None = None
    eventData: list[Any] | None = None
    eventType: str | None = None
    eventTime: str | None = None
    currentData: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DealHistory:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            eventData=data.get("eventData"),
            eventType=data.get("eventType"),
            eventTime=data.get("eventTime"),
            currentData=data.get("currentData"),
        )
