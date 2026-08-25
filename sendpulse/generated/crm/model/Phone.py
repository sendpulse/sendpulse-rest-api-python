from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Phone:
    id: int | None = None
    isMain: bool | None = None
    phone: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Phone:
        return cls(
            id=data.get("id"),
            isMain=data.get("isMain"),
            phone=data.get("phone"),
        )
