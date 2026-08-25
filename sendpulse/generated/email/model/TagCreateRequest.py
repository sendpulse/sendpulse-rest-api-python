from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TagCreateRequest:
    name: str | None = None
    color: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TagCreateRequest:
        return cls(
            name=data.get("name"),
            color=data.get("color"),
        )
