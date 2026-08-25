from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.smtp.model.DomainRecord import DomainRecord


@dataclass(slots=True)
class DomainListData:
    result: bool | None = None
    data: list[DomainRecord] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DomainListData:
        return cls(
            result=data.get("result"),
            data=[DomainRecord.from_dict(i) for i in data["data"]] if isinstance(data.get("data"), list) else None,
        )
