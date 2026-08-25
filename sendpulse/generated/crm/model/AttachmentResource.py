from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class AttachmentResource:
    id: int | None = None
    link: list[Any] | None = None
    entityId: int | None = None
    entityType: str | None = None
    createdAt: str | None = None
    updatedAt: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AttachmentResource:
        return cls(
            id=data.get("id"),
            link=data.get("link"),
            entityId=data.get("entityId"),
            entityType=data.get("entityType"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
        )
