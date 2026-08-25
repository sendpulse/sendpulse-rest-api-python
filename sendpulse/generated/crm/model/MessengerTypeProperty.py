from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class MessengerTypeProperty:
    pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MessengerTypeProperty:
        return cls()
