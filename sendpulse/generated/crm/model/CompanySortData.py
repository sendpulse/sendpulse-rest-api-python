from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CompanySortData:
    id: int | None = None
    companyName: str | None = None
    responsibleId: int | None = None
    address: str | None = None
    annualBusinessVolume: int | None = None
    currency: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CompanySortData:
        return cls(
            id=data.get("id"),
            companyName=data.get("companyName"),
            responsibleId=data.get("responsibleId"),
            address=data.get("address"),
            annualBusinessVolume=data.get("annualBusinessVolume"),
            currency=data.get("currency"),
        )
