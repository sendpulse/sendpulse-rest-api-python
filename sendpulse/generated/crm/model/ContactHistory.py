from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ContactHistory:
    id: int | None = None
    userId: int | None = None
    contactId: int | None = None
    eventType: str | None = None
    eventTime: str | None = None
    eventData: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactHistory:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            contactId=data.get("contactId"),
            eventType=data.get("eventType"),
            eventTime=data.get("eventTime"),
            eventData=data.get("eventData"),
        )
