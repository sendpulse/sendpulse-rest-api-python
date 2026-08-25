from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CustomTab:
    id: int | None = None
    name: str | None = None
    userId: int | None = None
    isVisible: bool | None = None
    isDefault: bool | None = None
    type: int | None = None
    entityType: int | None = None
    entityId: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CustomTab:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            userId=data.get("userId"),
            isVisible=data.get("isVisible"),
            isDefault=data.get("isDefault"),
            type=data.get("type"),
            entityType=data.get("entityType"),
            entityId=data.get("entityId"),
        )
