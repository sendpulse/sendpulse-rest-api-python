from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class VariableDefinition:
    name: str | None = None
    type: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> VariableDefinition:
        return cls(
            name=data.get("name"),
            type=data.get("type"),
        )
