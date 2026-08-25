from __future__ import annotations

import json
import time

import pytest

from sendpulse.auth.token_manager import TokenManager
from sendpulse.auth.token_storage import InMemoryTokenStorage, TokenData
from sendpulse.exception.exceptions import AuthException, ProtocolException
from sendpulse.http.response import Response
from tests.fixture.fake_http_client import FakeHttpClient


def _make_token_response(access_token: str = "tok123", expires_in: int = 3600) -> Response:
    body = json.dumps(
        {"access_token": access_token, "token_type": "Bearer", "expires_in": expires_in}
    )
    return Response(200, {}, body)


def _make_manager(
    http_client: FakeHttpClient,
    storage: InMemoryTokenStorage | None = None,
) -> TokenManager:
    return TokenManager(
        http_client=http_client,
        client_id="id123",
        client_secret="secret456",
        base_url="https://api.sendpulse.com",
        storage=storage or InMemoryTokenStorage(),
    )


def test_fetches_token_on_first_call() -> None:
    client = FakeHttpClient()
    client.queue(_make_token_response("first-token"))
    manager = _make_manager(client)

    token = manager.get_token()

    assert token == "first-token"
    assert client.call_count() == 1


def test_returns_cached_token_without_network_call() -> None:
    client = FakeHttpClient()
    client.queue(_make_token_response("cached-token"))
    manager = _make_manager(client)

    first = manager.get_token()
    second = manager.get_token()

    assert first == "cached-token"
    assert second == "cached-token"
    assert client.call_count() == 1


def test_refetches_when_token_expired() -> None:
    client = FakeHttpClient()
    storage = InMemoryTokenStorage()
    manager = _make_manager(client, storage)

    expired: TokenData = {
        "access_token": "old-token",
        "token_type": "Bearer",
        "expires_at": int(time.time()) - 1,
    }
    import hashlib
    key = hashlib.sha256(b"id123").hexdigest()
    storage.set(key, expired)

    client.queue(_make_token_response("new-token"))
    token = manager.get_token()

    assert token == "new-token"
    assert client.call_count() == 1


def test_refetches_after_invalidate() -> None:
    client = FakeHttpClient()
    client.queue(_make_token_response("first-token"))
    client.queue(_make_token_response("refreshed-token"))
    manager = _make_manager(client)

    manager.get_token()
    manager.invalidate()
    token = manager.get_token()

    assert token == "refreshed-token"
    assert client.call_count() == 2


def test_raises_auth_exception_on_non_200() -> None:
    client = FakeHttpClient()
    client.queue(Response(401, {}, '{"error": "invalid_client"}'))
    manager = _make_manager(client)

    with pytest.raises(AuthException) as exc_info:
        manager.get_token()

    assert exc_info.value.http_status == 401


def test_raises_protocol_exception_on_invalid_json() -> None:
    client = FakeHttpClient()
    client.queue(Response(200, {}, "not-json"))
    manager = _make_manager(client)

    with pytest.raises(ProtocolException, match="Failed to decode"):
        manager.get_token()


def test_raises_protocol_exception_on_missing_access_token() -> None:
    client = FakeHttpClient()
    client.queue(Response(200, {}, '{"token_type": "Bearer", "expires_in": 3600}'))
    manager = _make_manager(client)

    with pytest.raises(ProtocolException, match="Invalid OAuth"):
        manager.get_token()


def test_raises_protocol_exception_on_missing_expires_in() -> None:
    client = FakeHttpClient()
    client.queue(Response(200, {}, '{"access_token": "tok", "token_type": "Bearer"}'))
    manager = _make_manager(client)

    with pytest.raises(ProtocolException, match="Invalid OAuth"):
        manager.get_token()


def test_sends_correct_oauth_request() -> None:
    client = FakeHttpClient()
    client.queue(_make_token_response())
    manager = _make_manager(client)

    manager.get_token()

    req = client.last_request()
    assert req.method == "POST"
    assert req.uri == "https://api.sendpulse.com/oauth/access_token"
    assert "client_credentials" in (req.body or "")
    assert "id123" in (req.body or "")
