from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class History:
    eventType: str | None = None
    eventData: list[Any] | None = None
    date: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> History:
        return cls(
            eventType=data.get("eventType"),
            eventData=data.get("eventData"),
            date=data.get("date"),
        )
