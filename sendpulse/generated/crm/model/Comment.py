from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Comment:
    id: int | None = None
    userId: int | None = None
    text: str | None = None
    status: int | None = None
    createdAt: str | None = None
    updatedAt: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Comment:
        return cls(
            id=data.get("id"),
            userId=data.get("userId"),
            text=data.get("text"),
            status=data.get("status"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
        )
