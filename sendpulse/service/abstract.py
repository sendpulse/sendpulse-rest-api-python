from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sendpulse.client import Client
    from sendpulse.http.request import Request


class AbstractService:
    def __init__(self, client: Client) -> None:
        self._client = client

    def _send(self, request: Request) -> dict[str, Any]:
        result = self._client.send(request)
        return result if isinstance(result, dict) else {}

    def _send_list(self, request: Request) -> list[Any]:
        result = self._client.send(request)
        return result if isinstance(result, list) else []
