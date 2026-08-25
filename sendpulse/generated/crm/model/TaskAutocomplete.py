from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TaskAutocomplete:
    pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskAutocomplete:
        return cls()
