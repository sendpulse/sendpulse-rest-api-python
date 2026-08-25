from __future__ import annotations

import json
from typing import Any

from sendpulse.exception.exceptions import (
    ApiException,
    AuthException,
    ProtocolException,
    RateLimitException,
)
from sendpulse.http.response import Response


class ResponseValidator:
    def validate(self, response: Response) -> dict[str, Any] | list[Any]:
        status = response.status_code

        if 200 <= status < 300:
            return self._decode(response)

        if status in (401, 403):
            raise AuthException(status, response.body)

        if status == 429:
            raise RateLimitException(status, response.body)

        raise ApiException(status, response.body)

    def _decode(self, response: Response) -> dict[str, Any] | list[Any]:
        if not response.body:
            return {}

        try:
            data = json.loads(response.body)
        except json.JSONDecodeError as e:
            raise ProtocolException(f"Failed to decode response body: {e}") from e

        if isinstance(data, (dict, list)):
            return data
        return {}
