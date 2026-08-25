from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TaskTag:
    id: int | None = None
    name: str | None = None
    colorText: str | None = None
    colorBackground: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskTag:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            colorText=data.get("colorText"),
            colorBackground=data.get("colorBackground"),
        )
