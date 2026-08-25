from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ReferralStat:
    link: str | None = None
    count: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ReferralStat:
        return cls(
            link=data.get("link"),
            count=data.get("count"),
        )
