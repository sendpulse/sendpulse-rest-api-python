from __future__ import annotations

import hashlib
import json
import threading
import time
from urllib.parse import urlencode

from sendpulse.auth.protocol import TokenStorageProtocol
from sendpulse.auth.token_storage import TokenData
from sendpulse.exception.exceptions import AuthException, ProtocolException
from sendpulse.http.protocol import HttpClient
from sendpulse.http.request import Request


class TokenManager:
    EXPIRY_BUFFER = 300

    def __init__(
        self,
        http_client: HttpClient,
        client_id: str,
        client_secret: str,
        base_url: str,
        storage: TokenStorageProtocol,
    ) -> None:
        self._http = http_client
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url.rstrip("/")
        self._storage = storage
        self._storage_key = hashlib.sha256(client_id.encode()).hexdigest()
        self._invalidated = False
        self._lock = threading.Lock()

    def get_token(self) -> str:
        with self._lock:
            if not self._invalidated:
                cached = self._storage.get(self._storage_key)
                if cached and cached["expires_at"] > time.time() + self.EXPIRY_BUFFER:
                    return cached["access_token"]
            return self._fetch_and_store()

    def invalidate(self) -> None:
        with self._lock:
            self._invalidated = True
            self._storage.delete(self._storage_key)

    def _fetch_and_store(self) -> str:
        body = urlencode(
            {
                "grant_type": "client_credentials",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
            }
        )

        request = Request(
            method="POST",
            uri=f"{self._base_url}/oauth/access_token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            body=body,
        )

        response = self._http.send(request)

        if response.status_code != 200:
            raise AuthException(response.status_code, response.body, "OAuth token fetch failed")

        try:
            data: object = json.loads(response.body)
        except json.JSONDecodeError as e:
            raise ProtocolException(f"Failed to decode OAuth response: {e}") from e

        if (
            not isinstance(data, dict)
            or not isinstance(data.get("access_token"), str)
            or not isinstance(data.get("token_type"), str)
            or not isinstance(data.get("expires_in"), (int, float))
            or data["expires_in"] <= 0
        ):
            raise ProtocolException("Invalid OAuth token response shape")

        token: TokenData = {
            "access_token": data["access_token"],
            "token_type": data["token_type"],
            "expires_at": int(time.time()) + int(data["expires_in"]),
        }

        self._storage.set(self._storage_key, token)
        self._invalidated = False

        return token["access_token"]
