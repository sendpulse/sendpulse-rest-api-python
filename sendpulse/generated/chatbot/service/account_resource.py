from __future__ import annotations

from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class AccountResource(AbstractService):
    def get_account(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/account",
        ))
