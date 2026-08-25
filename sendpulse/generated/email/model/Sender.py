from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Sender:
    email: str | None = None
    name: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Sender:
        return cls(
            email=data.get("email"),
            name=data.get("name"),
        )
