from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.sms.model.NumbersImport import NumbersImport
from sendpulse.generated.sms.model.NumbersRemoval import NumbersRemoval
from sendpulse.generated.sms.model.ResultTrue import ResultTrue
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactsResource(AbstractService):
    def add_sms_numbers(self, body: dict[str, Any] | list[Any] | None = None) -> NumbersImport:
        return NumbersImport.from_dict(self._send(Request(
            method="POST",
            uri="/sms/numbers",
            body=json.dumps(body) if body else None,
        )))

    def update_sms_variables_batch(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="PUT",
            uri="/sms/numbers",
            body=json.dumps(body) if body else None,
        ))

    def remove_sms_numbers(self, body: dict[str, Any] | list[Any] | None = None) -> NumbersRemoval:
        return NumbersRemoval.from_dict(self._send(Request(
            method="DELETE",
            uri="/sms/numbers",
            body=json.dumps(body) if body else None,
        )))

    def add_sms_numbers_with_variables(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/sms/numbers/variables",
            body=json.dumps(body) if body else None,
        ))

    def update_contact_phone(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="PUT",
            uri=f"/addressbooks/{id}/phone",
            body=json.dumps(body) if body else None,
        )))

    def update_sms_variables_single(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri=f"/addressbooks/{id}/phones/variable",
            body=json.dumps(body) if body else None,
        )))

    def get_sms_number_info(self, addressBookId: int, phoneNumber: str) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/sms/numbers/info/{addressBookId}/{phoneNumber}",
        ))
