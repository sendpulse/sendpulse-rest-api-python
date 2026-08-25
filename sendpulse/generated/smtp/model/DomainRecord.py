from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DomainRecord:
    id: int | None = None
    user_id: int | None = None
    service_type: int | None = None
    service_value: str | None = None
    status: int | None = None
    is_default: bool | None = None
    ssl_type: int | None = None
    checks: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DomainRecord:
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            service_type=data.get("service_type"),
            service_value=data.get("service_value"),
            status=data.get("status"),
            is_default=data.get("is_default"),
            ssl_type=data.get("ssl_type"),
            checks=data.get("checks"),
        )
