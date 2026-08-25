from __future__ import annotations

from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DialogsResource(AbstractService):
    def get_dialogs(self, size: int | None = None, skip: int | None = None, search_after: str | None = None, order: str | None = None) -> dict[str, Any]:
        params = {k: v for k, v in {"size": size, "skip": skip, "search_after": search_after, "order": order}.items() if v is not None}
        return self._send(Request(
            method="GET",
            uri="/dialogs",
            params=params or None,
        ))
