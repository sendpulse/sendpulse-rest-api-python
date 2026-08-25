from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CostData:
    price: float | None = None
    currency: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CostData:
        return cls(
            price=data.get("price"),
            currency=data.get("currency"),
        )
