from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class SubscriberStats:
    statistic: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SubscriberStats:
        return cls(
            statistic=data.get("statistic"),
        )
