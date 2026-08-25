from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class BoardSteps:
    id: int | None = None
    name: str | None = None
    color: str | None = None
    order: int | None = None
    boardId: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BoardSteps:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            color=data.get("color"),
            order=data.get("order"),
            boardId=data.get("boardId"),
        )
