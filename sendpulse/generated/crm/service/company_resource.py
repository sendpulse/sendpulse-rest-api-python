from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class CompanyResource(AbstractService):
    def get_companies_short_data(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/companies/short-data",
            body=json.dumps(body) if body else None,
        ))

    def get_companies_list(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/companies/list",
            body=json.dumps(body) if body else None,
        ))

    def create_company(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/companies",
            body=json.dumps(body) if body else None,
        ))

    def get_company_by_id(self, companyId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/companies/{companyId}",
        ))

    def update_company(self, companyId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri=f"/companies/{companyId}",
            body=json.dumps(body) if body else None,
        ))

    def delete_company(self, companyId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/companies/{companyId}",
        ))
