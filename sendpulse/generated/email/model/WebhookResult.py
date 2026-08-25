from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class WebhookResult:
    success: bool | None = None
    data: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WebhookResult:
        return cls(
            success=data.get("success"),
            data=data.get("data"),
        )
