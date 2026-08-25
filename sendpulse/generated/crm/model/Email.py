from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Email:
    id: int | None = None
    isMain: bool | None = None
    email: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Email:
        return cls(
            id=data.get("id"),
            isMain=data.get("isMain"),
            email=data.get("email"),
        )
