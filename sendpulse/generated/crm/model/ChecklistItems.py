from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ChecklistItems:
    id: int | None = None
    name: str | None = None
    order: float | None = None
    isDone: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ChecklistItems:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            order=data.get("order"),
            isDone=data.get("isDone"),
        )
