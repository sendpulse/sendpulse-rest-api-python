from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Request:
    method: str
    uri: str
    headers: dict[str, str] = field(default_factory=dict)
    body: str | None = None
    params: dict[str, Any] | None = None
