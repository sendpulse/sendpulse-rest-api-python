from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EmailDetails:
    list_name: str | None = None
    source: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmailDetails:
        return cls(
            list_name=data.get("list_name"),
            source=data.get("source"),
        )
