from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EmailAcrossBooks:
    book_id: int | None = None
    email: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmailAcrossBooks:
        return cls(
            book_id=data.get("book_id"),
            email=data.get("email"),
        )
