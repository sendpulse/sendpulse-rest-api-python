from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Account:
    tariff: dict[str, Any] | None = None
    statistics: dict[str, Any] | None = None
    services: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Account:
        return cls(
            tariff=data.get("tariff"),
            statistics=data.get("statistics"),
            services=data.get("services"),
        )
