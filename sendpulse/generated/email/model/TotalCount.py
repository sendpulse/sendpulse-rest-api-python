from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TotalCount:
    total: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TotalCount:
        return cls(
            total=data.get("total"),
        )
