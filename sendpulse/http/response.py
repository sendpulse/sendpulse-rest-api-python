from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Response:
    status_code: int
    headers: dict[str, str]
    body: str
