# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] — 2026-08-25

Complete rewrite of `pysendpulse` as version 2.0.0.

### BC Breaks

- **License** — changed from Apache-2.0 to MIT.
- **Entry point changed** — use `from sendpulse import Client` instead of `from pysendpulse.pysendpulse import PySendPulse`.
- **Constructor** — `Client(client_id=..., client_secret=...)` or `Client(api_key=...)`; the old positional `(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)` signature is gone.
- **Service layer** — flat methods on the client (`add_campaign()`, `smtp_send_mail()`, etc.) replaced by typed facades (`email_service()`, `smtp_service()`, etc.).
- **Exceptions** — typed hierarchy (`AuthException`, `RateLimitException`, `ApiException`, `NetworkException`, `ProtocolException`) replaces the old generic error handling.
- **Python 3.11+** required (was 3.x without a strict minimum).
- **Storage** — Memcached/file backends replaced by `FileTokenStorage` and `InMemoryTokenStorage`.

### Added

- Typed service facades: `email_service()`, `smtp_service()`, `sms_service()`, `crm_service()`, `chatbot_service()`.
- Services and models generated from OpenAPI specs — all endpoints covered.
- `TokenStorage` protocol with `FileTokenStorage` (atomic write) and `InMemoryTokenStorage`.
- Auto-retry on `401` — cached token is invalidated and a fresh one fetched before retrying once.
- Context manager support (`with Client(...) as client:`).
- Custom `HttpClient` and `TokenStorage` injection points for testing and custom transports.

---

## [0.1.8] — 2025-02-11

- Fixed re-send request handling.

## [0.1.7] — 2023-07-21

- Updated version metadata.

## [0.1.6] — 2023-07-21

- Fixed response getter.

## [0.1.5] — 2023-03-31

- Version bump.

## [0.1.4] — 2022-07-01

- Added SMS functional methods.

## [0.1.3] — 2021-09-28

- Added Automation360 method.

## [0.1.2] — 2021-02-04

- Added custom token path support.

## [0.1.1] — 2020-06-10

- Release preparation.

## [0.1.0] — 2020-04-13

- Fixed SMS variables check.

## [0.0.9] — 2020-03-26

- Initial stable release.
