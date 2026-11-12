from __future__ import annotations

from sendpulse.http.request import Request
from sendpulse.http.response import Response


class FakeHttpClient:
    def __init__(self) -> None:
        self._queue: list[Response] = []
        self._sent: list[Request] = []

    def queue(self, *responses: Response) -> None:
        self._queue.extend(responses)

    def send(self, request: Request) -> Response:
        self._sent.append(request)
        if not self._queue:
            raise RuntimeError("FakeHttpClient: no response queued")
        return self._queue.pop(0)

    def last_request(self) -> Request:
        if not self._sent:
            raise RuntimeError("FakeHttpClient: no request sent")
        return self._sent[-1]

    def all_requests(self) -> list[Request]:
        return list(self._sent)

    def call_count(self) -> int:
        return len(self._sent)
