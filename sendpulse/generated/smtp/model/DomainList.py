from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.smtp.model.DomainListData import DomainListData


@dataclass(slots=True)
class DomainList:
    data: DomainListData | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DomainList:
        return cls(
            data=DomainListData.from_dict(data["data"]) if isinstance(data.get("data"), dict) else None,
        )
