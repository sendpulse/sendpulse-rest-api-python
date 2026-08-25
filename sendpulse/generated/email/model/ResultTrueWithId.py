from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ResultTrueWithId:
    result: bool | None = None
    id: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ResultTrueWithId:
        return cls(
            result=data.get("result"),
            id=data.get("id"),
        )
