from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactAttributesResource(AbstractService):
    def get_contact_attributes(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/contacts/attributes",
        ))

    def create_contact_attribute(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/contacts/attributes",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_attribute(self, attributeId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/contacts/attributes/{attributeId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_contact_attribute(self, attributeId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/contacts/attributes/{attributeId}",
        ))
