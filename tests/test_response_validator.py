import pytest

from sendpulse.exception.exceptions import (
    ApiException,
    AuthException,
    ProtocolException,
    RateLimitException,
)
from sendpulse.http.response import Response
from sendpulse.response.validator import ResponseValidator


@pytest.fixture
def validator() -> ResponseValidator:
    return ResponseValidator()


def test_returns_decoded_dict_on_200(validator: ResponseValidator) -> None:
    response = Response(200, {}, '{"id": 1, "name": "test"}')
    assert validator.validate(response) == {"id": 1, "name": "test"}


def test_returns_empty_dict_on_empty_body(validator: ResponseValidator) -> None:
    response = Response(200, {}, "")
    assert validator.validate(response) == {}


def test_returns_empty_dict_on_non_dict_json(validator: ResponseValidator) -> None:
    response = Response(200, {}, '"just-a-string"')
    assert validator.validate(response) == {}


def test_201_is_treated_as_success(validator: ResponseValidator) -> None:
    response = Response(201, {}, '{"created": true}')
    assert validator.validate(response) == {"created": True}


def test_401_raises_auth_exception(validator: ResponseValidator) -> None:
    with pytest.raises(AuthException) as exc_info:
        validator.validate(Response(401, {}, '{"error": "Unauthorized"}'))
    assert exc_info.value.http_status == 401


def test_403_raises_auth_exception(validator: ResponseValidator) -> None:
    with pytest.raises(AuthException) as exc_info:
        validator.validate(Response(403, {}, '{"error": "Forbidden"}'))
    assert exc_info.value.http_status == 403


def test_429_raises_rate_limit_exception(validator: ResponseValidator) -> None:
    with pytest.raises(RateLimitException) as exc_info:
        validator.validate(Response(429, {}, '{"error": "Too Many Requests"}'))
    assert exc_info.value.http_status == 429


def test_400_raises_api_exception(validator: ResponseValidator) -> None:
    with pytest.raises(ApiException) as exc_info:
        validator.validate(Response(400, {}, '{"error": "Bad Request"}'))
    assert exc_info.value.http_status == 400


def test_500_raises_api_exception(validator: ResponseValidator) -> None:
    with pytest.raises(ApiException) as exc_info:
        validator.validate(Response(500, {}, "Internal Server Error"))
    assert exc_info.value.http_status == 500


def test_invalid_json_raises_protocol_exception(validator: ResponseValidator) -> None:
    with pytest.raises(ProtocolException, match="Failed to decode"):
        validator.validate(Response(200, {}, "not-json{"))


def test_raw_body_preserved_on_api_exception(validator: ResponseValidator) -> None:
    body = '{"message": "validation failed"}'
    with pytest.raises(ApiException) as exc_info:
        validator.validate(Response(422, {}, body))
    assert exc_info.value.raw_body == body
