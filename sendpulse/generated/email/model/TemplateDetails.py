from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TemplateDetails:
    id: str | None = None
    name: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TemplateDetails:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
        )
