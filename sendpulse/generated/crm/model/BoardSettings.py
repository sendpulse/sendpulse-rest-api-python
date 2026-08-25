from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class BoardSettings:
    id: int | None = None
    name: str | None = None
    value: str | None = None
    boardId: float | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BoardSettings:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            value=data.get("value"),
            boardId=data.get("boardId"),
        )
