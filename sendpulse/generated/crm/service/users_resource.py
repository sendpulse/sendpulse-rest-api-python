from __future__ import annotations

from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class UsersResource(AbstractService):
    def get_users(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/users",
        ))
