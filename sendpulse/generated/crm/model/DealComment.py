from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.EntityAttachment import EntityAttachment


@dataclass(slots=True)
class DealComment:
    id: int | None = None
    userId: int | None = None
    eventData: dict[str, Any] | None = None
    status: int | None = None
    eventTime: str | None = None
    createdAt: str | None = None
    updatedAt: str | None = None
    attachments: list[EntityAttachment] | None = None
    childCount: int | None = None
    childUsers: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DealComment:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            eventData=data.get("eventData"),
            status=data.get("status"),
            eventTime=data.get("eventTime"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
            attachments=[EntityAttachment.from_dict(i) for i in data["attachments"]] if isinstance(data.get("attachments"), list) else None,
            childCount=data.get("childCount"),
            childUsers=data.get("childUsers"),
        )
