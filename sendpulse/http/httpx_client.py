from __future__ import annotations

import httpx

from sendpulse.exception.exceptions import NetworkException
from sendpulse.http.request import Request
from sendpulse.http.response import Response


class HttpxClient:
    def __init__(
        self,
        connect_timeout: float = 10.0,
        request_timeout: float = 30.0,
    ) -> None:
        self._client = httpx.Client(
            timeout=httpx.Timeout(request_timeout, connect=connect_timeout),
            verify=True,
            follow_redirects=False,
        )

    def send(self, request: Request) -> Response:
        try:
            r = self._client.request(
                method=request.method,
                url=request.uri,
                headers=request.headers,
                content=request.body,
                params=request.params,
            )
        except httpx.TransportError as e:
            raise NetworkException(str(e)) from e

        return Response(
            status_code=r.status_code,
            headers=dict(r.headers),
            body=r.text,
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> HttpxClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
