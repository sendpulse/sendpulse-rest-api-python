from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote, urlparse

from sendpulse.auth.auth import ApiKeyAuth, OAuthAuth
from sendpulse.auth.protocol import TokenStorageProtocol
from sendpulse.auth.token_manager import TokenManager
from sendpulse.auth.token_storage import FileTokenStorage
from sendpulse.config import Config
from sendpulse.http.httpx_client import HttpxClient
from sendpulse.http.protocol import HttpClient
from sendpulse.http.request import Request
from sendpulse.resource import Resource
from sendpulse.resources import OperationMap, load_operations
from sendpulse.response.validator import ResponseValidator

_BASE_URL = "https://api.sendpulse.com"

if TYPE_CHECKING:
    # Phantom service attributes for IDE autocomplete; resolved at runtime by
    # __getattr__. Overridden by generated stubs when present.
    from sendpulse.stubs import Chatbot, Crm, Email, Sms, Smtp


class Client:
    """Thin SendPulse REST client.

    Two ways to call the API:

    * Chained operation surface (discoverable, validated):
        client.crm.deals.getDeal({"dealId": 5})
    * Raw HTTP verbs (escape hatch for anything not in the map):
        client.get("/sms/senders")
        client.post("/sms/send", {"phones": [...], "body": "hi"})
    """

    def __init__(
        self,
        api_key: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        connect_timeout: float = 10.0,
        request_timeout: float = 30.0,
        cache_dir: str | None = None,
        token_storage: TokenStorageProtocol | None = None,
        http_client: HttpClient | None = None,
    ) -> None:
        self._config = Config(
            api_key=api_key,
            client_id=client_id,
            client_secret=client_secret,
            connect_timeout=connect_timeout,
            request_timeout=request_timeout,
            cache_dir=cache_dir,
        )
        self._http: HttpClient = http_client or HttpxClient(
            connect_timeout=self._config.connect_timeout,
            request_timeout=self._config.request_timeout,
        )
        self._auth = self._build_auth(token_storage)
        self._validator = ResponseValidator()

    if TYPE_CHECKING:
        crm: Crm
        email: Email
        sms: Sms
        smtp: Smtp
        chatbot: Chatbot

    def __getattr__(self, name: str) -> Resource:
        if name.startswith("_"):
            raise AttributeError(name)
        return Resource(self, name)

    # ── Mapped operation dispatch ─────────────────────────────────────────────

    def call_operation(self, key: str, params: dict[str, Any] | None = None) -> dict[str, Any] | list[Any]:
        params = params or {}
        operations = self._operations()

        op = operations.get(key)
        if op is None:
            raise ValueError(f"Unknown operation: {key}")

        path: str = op["path"]
        method: str = op["method"]
        query: dict[str, Any] = {}
        body: dict[str, Any] = {}
        declared: dict[str, str] = op.get("params", {})

        for name, type_ in declared.items():
            in_path = "{" + name + "}" in path
            required = in_path or type_.endswith("!")

            if name not in params:
                if required:
                    raise ValueError(f"Missing required parameter '{name}' for {key}")
                continue

            value = params[name]

            if in_path:
                if not isinstance(value, (str, int, float, bool)):
                    raise ValueError(f"Path parameter '{name}' for {key} must be scalar")
                path = path.replace("{" + name + "}", quote(str(value), safe=""))
            elif method == "GET":
                query[name] = value
            else:
                body[name] = value

        # Pass undeclared params through untouched (query for GET, body otherwise).
        for name, value in params.items():
            if name in declared:
                continue
            if method == "GET":
                query[name] = value
            else:
                body[name] = value

        if method == "GET":
            return self.get(path, query)
        if method == "POST":
            return self.post(path, body)
        if method == "PUT":
            return self.put(path, body)
        if method == "PATCH":
            return self.patch(path, body)
        if method == "DELETE":
            return self.delete(path, body)
        raise ValueError(f"Unsupported method '{method}' for {key}")

    # ── Raw HTTP verbs ────────────────────────────────────────────────────────

    def get(
        self, path: str, query: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> dict[str, Any] | list[Any]:
        return self.request("GET", path, params=query or None, headers=headers)

    def post(
        self, path: str, body: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> dict[str, Any] | list[Any]:
        return self.request("POST", path, body=self._encode_body(body), headers=headers)

    def put(
        self, path: str, body: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> dict[str, Any] | list[Any]:
        return self.request("PUT", path, body=self._encode_body(body), headers=headers)

    def patch(
        self, path: str, body: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> dict[str, Any] | list[Any]:
        return self.request("PATCH", path, body=self._encode_body(body), headers=headers)

    def delete(
        self, path: str, body: dict[str, Any] | None = None, headers: dict[str, str] | None = None
    ) -> dict[str, Any] | list[Any]:
        return self.request("DELETE", path, body=self._encode_body(body), headers=headers)

    def request(
        self,
        method: str,
        path: str,
        body: str | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any] | list[Any]:
        return self.send(
            Request(
                method=method.upper(),
                uri=path,
                headers=headers or {},
                body=body,
                params=params,
            )
        )

    @staticmethod
    def _encode_body(body: dict[str, Any] | None) -> str | None:
        return json.dumps(body) if body else None

    # ── Transport ─────────────────────────────────────────────────────────────

    def send(self, request: Request) -> dict[str, Any] | list[Any]:
        authed = self._with_auth(request)
        response = self._http.send(authed)

        if response.status_code == 401 and self._auth.supports_refresh():
            self._auth.invalidate()
            authed = self._with_auth(request)
            response = self._http.send(authed)

        return self._validator.validate(response)

    def close(self) -> None:
        close = getattr(self._http, "close", None)
        if callable(close):
            close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    # ── Internals ─────────────────────────────────────────────────────────────

    def _operations(self) -> OperationMap:
        return load_operations()

    def _with_auth(self, request: Request) -> Request:
        uri = request.uri.lstrip("/")
        if urlparse(uri).scheme:
            raise ValueError(f"Request URI must be a relative path, got: {uri!r}")

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            **request.headers,
            # Applied last so caller headers cannot override SDK authentication.
            "Authorization": self._auth.get_authorization_header(),
        }
        return Request(
            method=request.method,
            uri=f"{_BASE_URL}/{uri}",
            headers=headers,
            body=request.body,
            params=request.params,
        )

    def _build_auth(self, token_storage: TokenStorageProtocol | None) -> ApiKeyAuth | OAuthAuth:
        if not self._config.is_oauth:
            return ApiKeyAuth(self._config.api_key or "")

        storage: TokenStorageProtocol = token_storage or FileTokenStorage(self._config.cache_dir)
        manager = TokenManager(
            http_client=self._http,
            client_id=self._config.client_id or "",
            client_secret=self._config.client_secret or "",
            base_url=_BASE_URL,
            storage=storage,
        )
        return OAuthAuth(manager)
