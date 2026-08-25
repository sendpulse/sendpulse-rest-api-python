from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class SenderActivationResponse:
    result: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SenderActivationResponse:
        return cls(
            result=data.get("result"),
        )
