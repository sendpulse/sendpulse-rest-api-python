from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CommentCompany:
    id: int | None = None
    message: str | None = None
    createdAt: str | None = None
    updatedAt: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CommentCompany:
        return cls(
            id=data.get("id"),
            message=data.get("message"),
            createdAt=data.get("createdAt"),
            updatedAt=data.get("updatedAt"),
        )
