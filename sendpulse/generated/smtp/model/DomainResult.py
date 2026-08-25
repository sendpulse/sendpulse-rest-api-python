from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.smtp.model.ResultTrue import ResultTrue


@dataclass(slots=True)
class DomainResult:
    data: ResultTrue | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DomainResult:
        return cls(
            data=ResultTrue.from_dict(data["data"]) if isinstance(data.get("data"), dict) else None,
        )
