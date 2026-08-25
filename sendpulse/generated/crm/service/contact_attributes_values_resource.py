from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactAttributesValuesResource(AbstractService):
    def batch_store_contact_attribute_values(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/attributes/batch",
            body=json.dumps(body) if body else None,
        ))
