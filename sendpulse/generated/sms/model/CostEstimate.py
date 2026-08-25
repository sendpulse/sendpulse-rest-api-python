from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.sms.model.CostData import CostData


@dataclass(slots=True)
class CostEstimate:
    result: bool | None = None
    data: CostData | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CostEstimate:
        return cls(
            result=data.get("result"),
            data=CostData.from_dict(data["data"]) if isinstance(data.get("data"), dict) else None,
        )
