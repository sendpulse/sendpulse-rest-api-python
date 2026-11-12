"""Dict-call dispatch: client.{service}.{resource}.{method}({...}) -> HTTP request."""
from __future__ import annotations

import json

import pytest

from sendpulse.client import Client
from sendpulse.http.response import Response
from tests.fixture.fake_http_client import FakeHttpClient


def _client(http: FakeHttpClient) -> Client:
    return Client(api_key="key", http_client=http)


def _ok() -> Response:
    return Response(200, {}, '{"ok": true}')


def test_path_param_is_substituted() -> None:
    http = FakeHttpClient()
    http.queue(_ok())
    _client(http).sms.campaigns.getSmsCampaignInfo({"id": 5})

    req = http.last_request()
    assert req.method == "GET"
    assert req.uri == "https://api.sendpulse.com/sms/campaigns/info/5"
    assert req.body is None


def test_declared_query_params_are_routed_to_query() -> None:
    http = FakeHttpClient()
    http.queue(_ok())
    _client(http).sms.campaigns.getSmsCampaigns({"dateFrom": "2024-01-01", "dateTo": "2024-02-01"})

    assert http.last_request().params == {"dateFrom": "2024-01-01", "dateTo": "2024-02-01"}


def test_undeclared_params_go_to_body_on_post() -> None:
    http = FakeHttpClient()
    http.queue(_ok())
    _client(http).sms.campaigns.sendSmsToNumbers({"phones": ["+100"], "body": "hi"})

    req = http.last_request()
    assert req.method == "POST"
    assert req.uri.endswith("/sms/send")
    assert json.loads(req.body or "") == {"phones": ["+100"], "body": "hi"}
    assert req.params is None


def test_multiple_path_params_are_url_encoded() -> None:
    http = FakeHttpClient()
    http.queue(_ok())
    _client(http).sms.contacts.getSmsNumberInfo({"addressBookId": 7, "phoneNumber": "+1 23"})

    assert http.last_request().uri.endswith("/sms/numbers/info/7/%2B1%2023")


def test_missing_required_param_raises() -> None:
    http = FakeHttpClient()
    with pytest.raises(ValueError, match="Missing required parameter 'id'"):
        _client(http).sms.campaigns.cancelSmsCampaign({})


def test_unknown_operation_raises() -> None:
    http = FakeHttpClient()
    with pytest.raises(ValueError, match="Unknown operation"):
        # Intentionally an operation the stub doesn't declare — the runtime must reject it.
        _client(http).sms.campaigns.noSuchThing({})  # type: ignore[attr-defined]


def test_path_param_defaults_to_empty_dict() -> None:
    http = FakeHttpClient()
    http.queue(_ok())
    # getSmsSenders has no params; callable with no argument.
    _client(http).sms.configuration.getSmsSenders()

    assert http.last_request().uri.endswith("/sms/senders")


def test_decoded_json_is_returned() -> None:
    http = FakeHttpClient()
    http.queue(Response(200, {}, '{"id": 1}'))
    result = _client(http).sms.campaigns.getSmsCampaignInfo({"id": 1})
    assert result == {"id": 1}


@pytest.mark.parametrize(
    "verb,method",
    [("get", "GET"), ("post", "POST"), ("put", "PUT"), ("patch", "PATCH"), ("delete", "DELETE")],
)
def test_raw_verbs_map_to_methods(verb: str, method: str) -> None:
    http = FakeHttpClient()
    http.queue(_ok())
    client = _client(http)
    getattr(client, verb)("/x", {"a": 1})

    req = http.last_request()
    assert req.method == method
    if method == "GET":
        assert req.params == {"a": 1}
        assert req.body is None
    else:
        assert json.loads(req.body or "") == {"a": 1}
