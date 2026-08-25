from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TemplateCreation:
    result: bool | None = None
    real_id: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TemplateCreation:
        return cls(
            result=data.get("result"),
            real_id=data.get("real_id"),
        )
