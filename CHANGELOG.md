# Changelog

All notable changes to this project are documented here.

## 2.0.0

Complete rewrite as a **thin client**. This is a breaking change.

### Changed
- **Import name is now `sendpulse`** (was `pysendpulse`). The PyPI distribution
  stays `pysendpulse` (`pip install pysendpulse`).
- New calling convention — a **chained surface** backed by a generated operation
  map: `client.crm.deals.getDeal({"dealId": 5})`. One dict argument per call;
  path/query params routed automatically, everything else sent as the JSON body.
- Raw HTTP verbs available for any endpoint: `client.get/post/put/patch/delete`,
  `client.request(...)`, `client.send(Request(...))`.
- Responses are returned as decoded JSON (`dict` or `list`).
- Typed exception hierarchy under `sendpulse.SendPulseError`: `AuthException`
  (401/403), `RateLimitException` (429), `ApiException` (other 4xx/5xx),
  `NetworkException`, `ProtocolException`.
- OAuth 2.0 with automatic token caching and one-shot refresh on `401`; API-key
  auth; swappable HTTP client (`httpx` by default) and token storage.
- Requires Python ≥ 3.11. Single runtime dependency: `httpx`.

### Added
- IDE autocomplete via generated `sendpulse/stubs.pyi` (chain + method names, with
  each operation's route and parameters in its docstring).
- `llms.txt` — machine-readable endpoint catalog for AI coding assistants.
- mypy strict, ruff, and a full pytest suite.

### Removed
- The old `pysendpulse` single-module client and its API.
