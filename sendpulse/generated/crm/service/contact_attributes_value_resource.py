from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactAttributesValueResource(AbstractService):
    def get_contact_attributes_by_id(self, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/contacts/{contactId}/attributes",
        ))

    def add_contact_attribute_value(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/attributes",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_attribute_value(self, contactId: int, attributeId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contacts/{contactId}/attributes/{attributeId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_contact_attribute_value(self, contactId: int, attributeId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/{contactId}/attributes/{attributeId}",
        ))
