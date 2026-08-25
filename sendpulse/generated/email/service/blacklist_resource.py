from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.ResultTrue import ResultTrue
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class BlacklistResource(AbstractService):
    def get_blacklist(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/blacklist",
        ))

    def add_to_blacklist(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri="/blacklist",
            body=json.dumps(body) if body else None,
        )))

    def remove_from_blacklist(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri="/blacklist",
            body=json.dumps(body) if body else None,
        )))
