# Scalar API

Generated Python SDK for Scalar API.
API for managing Scalar platform resources.

## TypeScript SDK

For TypeScript, we provide a SDK that makes using our API even easier.

### Install

```bash
npm add @scalar/sdk
```

### Get a Scalar API key

Create an API key in your Scalar account:

- Dashboard: https://dashboard.scalar.com/account
- Store it in `.env`, for example:

```bash
SCALAR_API_KEY=your_personal_token
```

### Exchange your API key for an access token

The personal token is not an access token. Exchange it first with `postv1AuthExchange`.

If you use the personal token directly for authenticated API calls, the API returns `401 Invalid authentication token`.

```ts
import { Scalar } from '@scalar/sdk'

const scalar = new Scalar()

const exchange = await scalar.auth.postv1AuthExchange({
  personalToken: process.env.SCALAR_API_KEY!,
})

const accessToken = exchange.accessToken
```

### Use the access token

Construct a second client with bearer auth. Use this authenticated client for API calls.

```ts
import { Scalar } from '@scalar/sdk'

const scalar = new Scalar()

const exchange = await scalar.auth.postv1AuthExchange({
  personalToken: process.env.SCALAR_API_KEY!,
})

const authedScalar = new Scalar({
  bearerAuth: exchange.accessToken,
})
```

### Notes

- The exchange request itself can be made from a client constructed with no arguments (`new Scalar()`).
- The exchanged access token is valid for 12 hours.
- Timestamps are Unix seconds.

### Read more

- [@scalar/sdk on npm](https://www.npmjs.com/package/@scalar/sdk)

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](./api.md)
- [Async](#async)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install scalarApi
```

<br />

## Usage

```python
import os

from scalar_api import ScalarApi

client = ScalarApi(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)

registry = client.registry.list_all_api_documents()
print(registry)
```

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`AsyncScalarApi`) exposing the same resource tree with `await`.

```python
import asyncio

from scalar_api import AsyncScalarApi

async def main() -> None:
    client = AsyncScalarApi()
    registry = await client.registry.list_all_api_documents()

asyncio.run(main())
```

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `string \| provider` | - | Credential for the BearerAuth scheme. Defaults to BEARER_AUTH. |

Declared schemes:

- `BearerAuth` bearer token

<br />

## Errors

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from scalar_api import APIStatusError

try:
    registry = client.registry.list_all_api_documents()
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

Documented error statuses: `400`, `401`, `403`, `404`, `422`, `500`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from scalar_api import ScalarApi

client = ScalarApi(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `str \| None` | `os.environ.get("BEARER_AUTH")` | Credential for the BearerAuth scheme. |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `SCALAR_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `scalar_api` logger.

<br />

## Requirements

- Python 3.8 or newer

Powered by Scalar.


## Contributions

This SDK is generated programmatically. Manual edits to generated files will be
overwritten on the next build.

### SDK created by [Scalar](https://www.scalar.com/?utm_source=scalar-typescript-sdk-python&utm_campaign=sdk)
