from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EmailInfoShort:
    book_id: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmailInfoShort:
        return cls(
            book_id=data.get("book_id"),
        )
