from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TaskTotals:
    total: int | None = None
    steps: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskTotals:
        return cls(
            total=data.get("total"),
            steps=data.get("steps"),
        )
