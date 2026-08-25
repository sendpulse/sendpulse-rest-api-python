from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactEmailAddressesResource(AbstractService):
    def add_contact_emails(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/emails",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_email(self, contactId: int, emailId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contacts/{contactId}/emails/{emailId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_contact_email(self, contactId: int, emailId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/{contactId}/emails/{emailId}",
        ))
