from __future__ import annotations

from typing import Protocol

from sendpulse.http.request import Request
from sendpulse.http.response import Response


class HttpClient(Protocol):
    def send(self, request: Request) -> Response: ...
