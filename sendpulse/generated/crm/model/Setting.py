from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Setting:
    name: str | None = None
    value: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Setting:
        return cls(
            name=data.get("name"),
            value=data.get("value"),
        )
