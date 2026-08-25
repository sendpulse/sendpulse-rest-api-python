from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.ContactsAutocomplete import ContactsAutocomplete
from sendpulse.generated.crm.model.DealsAutocomplete import DealsAutocomplete
from sendpulse.generated.crm.model.TaskAutocomplete import TaskAutocomplete


@dataclass(slots=True)
class TasksConnection:
    tasks: TaskAutocomplete | None = None
    deals: DealsAutocomplete | None = None
    contacts: ContactsAutocomplete | None = None
    subTasks: TaskAutocomplete | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TasksConnection:
        return cls(
            tasks=TaskAutocomplete.from_dict(data["tasks"]) if isinstance(data.get("tasks"), dict) else None,
            deals=DealsAutocomplete.from_dict(data["deals"]) if isinstance(data.get("deals"), dict) else None,
            contacts=ContactsAutocomplete.from_dict(data["contacts"]) if isinstance(data.get("contacts"), dict) else None,
            subTasks=TaskAutocomplete.from_dict(data["subTasks"]) if isinstance(data.get("subTasks"), dict) else None,
        )
