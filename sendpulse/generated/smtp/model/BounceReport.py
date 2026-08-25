from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.smtp.model.BounceEmail import BounceEmail


@dataclass(slots=True)
class BounceReport:
    total: int | None = None
    emails: list[BounceEmail] | None = None
    request_limit: int | None = None
    found: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BounceReport:
        return cls(
            total=data.get("total"),
            emails=[BounceEmail.from_dict(i) for i in data["emails"]] if isinstance(data.get("emails"), list) else None,
            request_limit=data.get("request_limit"),
            found=data.get("found"),
        )
