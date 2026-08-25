from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactsMessengersResource(AbstractService):
    def add_contact_messenger(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/messengers",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_messenger(self, contactId: int, messengerId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contacts/{contactId}/messengers/{messengerId}",
            body=json.dumps(body) if body else None,
        ))

    def remove_contact_messenger(self, contactId: int, messengerId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/{contactId}/messengers/{messengerId}",
        ))
