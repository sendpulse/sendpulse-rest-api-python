from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class SuccessResponse:
    success: bool | None = None
    data: Any = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SuccessResponse:
        return cls(
            success=data.get("success"),
            data=data.get("data"),
        )
