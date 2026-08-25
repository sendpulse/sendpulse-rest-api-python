from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactPhoneNumberResource(AbstractService):
    def add_contact_phone(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/phones",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_phone(self, contactId: int, phoneId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contacts/{contactId}/phones/{phoneId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_contact_phone(self, contactId: int, phoneId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/{contactId}/phones/{phoneId}",
        ))
