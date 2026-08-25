from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.EntityAttachment import EntityAttachment


@dataclass(slots=True)
class ContactComment:
    id: int | None = None
    userId: int | None = None
    text: str | None = None
    createdAt: str | None = None
    updatedAt: str | None = None
    attachments: EntityAttachment | None = None
    childCount: int | None = None
    childUsers: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactComment:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            text=data.get("text"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
            attachments=EntityAttachment.from_dict(data["attachments"]) if isinstance(data.get("attachments"), dict) else None,
            childCount=data.get("childCount"),
            childUsers=data.get("childUsers"),
        )
