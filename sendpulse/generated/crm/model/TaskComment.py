from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.EntityAttachment import EntityAttachment


@dataclass(slots=True)
class TaskComment:
    id: int | None = None
    name: str | None = None
    taskId: int | None = None
    userId: int | None = None
    body: str | None = None
    createdAt: str | None = None
    updatedAt: str | None = None
    attachments: list[EntityAttachment] | None = None
    childCount: int | None = None
    childUsers: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskComment:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            taskId=data.get("taskId"),
            userId=data.get("userId"),
            body=data.get("body"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
            attachments=[EntityAttachment.from_dict(i) for i in data["attachments"]] if isinstance(data.get("attachments"), list) else None,
            childCount=data.get("childCount"),
            childUsers=data.get("childUsers"),
        )
