from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Error:
    message: str | None = None
    error_code: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Error:
        return cls(
            message=data.get("message"),
            error_code=data.get("error_code"),
        )
