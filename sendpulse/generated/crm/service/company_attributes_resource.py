from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class CompanyAttributesResource(AbstractService):
    def get_company_attributes(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/companies/attributes",
        ))

    def create_company_attribute(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/companies/attributes",
            body=json.dumps(body) if body else None,
        ))

    def update_company_attribute(self, attributeId: int, attribute: str, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/companies/attributes/{attribute}",
            body=json.dumps(body) if body else None,
        ))

    def delete_company_attribute(self, attributeId: int, attribute: str) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/companies/attributes/{attribute}",
        ))
