from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class NumbersImport:
    result: bool | None = None
    counters: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> NumbersImport:
        return cls(
            result=data.get("result"),
            counters=data.get("counters"),
        )
