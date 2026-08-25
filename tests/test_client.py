from __future__ import annotations

import json

import pytest

from sendpulse.auth.token_storage import InMemoryTokenStorage
from sendpulse.client import Client
from sendpulse.exception.exceptions import ApiException, AuthException
from sendpulse.http.request import Request
from sendpulse.http.response import Response
from tests.fixture.fake_http_client import FakeHttpClient


def _ok(body: dict[str, object]) -> Response:
    return Response(200, {}, json.dumps(body))


def _make_client(http: FakeHttpClient, *, oauth: bool = False) -> Client:
    if oauth:
        storage = InMemoryTokenStorage()
        http.queue(Response(200, {}, json.dumps({
            "access_token": "tok", "token_type": "Bearer", "expires_in": 3600,
        })))
        return Client(
            client_id="id", client_secret="secret",
            http_client=http, token_storage=storage,
        )
    return Client(api_key="test-key", http_client=http)


# ── Authorization header ──────────────────────────────────────────────────────

def test_api_key_sets_bearer_header() -> None:
    http = FakeHttpClient()
    http.queue(_ok({}))
    client = _make_client(http)

    client.send(Request(method="GET", uri="/test"))

    assert http.last_request().headers["Authorization"] == "Bearer test-key"


def test_oauth_sets_bearer_header() -> None:
    http = FakeHttpClient()
    client = _make_client(http, oauth=True)  # queues token fetch first
    http.queue(_ok({}))

    client.send(Request(method="GET", uri="/test"))

    req = http.last_request()
    assert req.headers["Authorization"] == "Bearer tok"


# ── URI construction ──────────────────────────────────────────────────────────

def test_base_url_is_prepended_to_uri() -> None:
    http = FakeHttpClient()
    http.queue(_ok({}))
    client = Client(api_key="key", http_client=http)

    client.send(Request(method="GET", uri="/smtp/emails"))

    assert http.last_request().uri == "https://api.sendpulse.com/smtp/emails"


def test_leading_slash_on_uri_is_not_doubled() -> None:
    http = FakeHttpClient()
    http.queue(_ok({}))
    client = Client(api_key="key", http_client=http)

    client.send(Request(method="GET", uri="/smtp/emails"))

    assert "//smtp" not in http.last_request().uri


# ── Default headers ───────────────────────────────────────────────────────────

def test_content_type_and_accept_headers_are_set() -> None:
    http = FakeHttpClient()
    http.queue(_ok({}))
    client = _make_client(http)

    client.send(Request(method="POST", uri="/test"))

    req = http.last_request()
    assert req.headers["Content-Type"] == "application/json"
    assert req.headers["Accept"] == "application/json"


def test_caller_headers_override_defaults() -> None:
    http = FakeHttpClient()
    http.queue(_ok({}))
    client = _make_client(http)

    client.send(Request(method="GET", uri="/test", headers={"Accept": "text/plain"}))

    assert http.last_request().headers["Accept"] == "text/plain"


# ── 401 retry with OAuth ──────────────────────────────────────────────────────

def test_oauth_retries_on_401() -> None:
    http = FakeHttpClient()
    def _token(t: str) -> Response:
        return Response(200, {}, json.dumps(
            {"access_token": t, "token_type": "Bearer", "expires_in": 3600}
        ))

    # token fetch → 401 on first call → token refresh → success
    http.queue(
        _token("tok1"),
        Response(401, {}, "Unauthorized"),
        _token("tok2"),
        _ok({"ok": True}),
    )
    storage = InMemoryTokenStorage()
    client = Client(client_id="id", client_secret="secret", http_client=http, token_storage=storage)

    result = client.send(Request(method="GET", uri="/test"))

    assert result == {"ok": True}
    assert http.call_count() == 4  # token + original + token refresh + retry


def test_api_key_does_not_retry_on_401() -> None:
    http = FakeHttpClient()
    http.queue(Response(401, {}, "Unauthorized"))
    client = _make_client(http)

    with pytest.raises(AuthException):
        client.send(Request(method="GET", uri="/test"))

    assert http.call_count() == 1


# ── Response parsing ──────────────────────────────────────────────────────────

def test_returns_parsed_json_body() -> None:
    http = FakeHttpClient()
    http.queue(_ok({"id": 42, "name": "test"}))
    client = _make_client(http)

    result = client.send(Request(method="GET", uri="/test"))

    assert result == {"id": 42, "name": "test"}


def test_raises_api_exception_on_500() -> None:
    http = FakeHttpClient()
    http.queue(Response(500, {}, "Internal Server Error"))
    client = _make_client(http)

    with pytest.raises(ApiException) as exc_info:
        client.send(Request(method="GET", uri="/test"))

    assert exc_info.value.http_status == 500


# ── Service lazy caching ──────────────────────────────────────────────────────

def test_email_service_returns_same_instance() -> None:
    client = Client(api_key="key", http_client=FakeHttpClient())
    assert client.email_service() is client.email_service()


def test_smtp_service_returns_same_instance() -> None:
    client = Client(api_key="key", http_client=FakeHttpClient())
    assert client.smtp_service() is client.smtp_service()
