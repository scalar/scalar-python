---
name: scalar-api-python-sdk
description: "Python SDK for Scalar API. Use when writing Python code that calls Scalar API with the scalar-sdk package: installing it, constructing and authenticating the client, and calling API operations."
---

# Scalar API Python SDK

Generated Python client for Scalar API, published as `scalar-sdk`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install scalar-sdk
```

## Client setup and authentication

```python
import os

from scalar_sdk import Scalar

client = Scalar(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `bearer_auth` (env: `BEARER_AUTH`) — Credential for the BearerAuth scheme.

## Calling operations

```python
import os

from scalar_sdk import Scalar

client = Scalar(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)

registry = client.registry.list_all_api_documents()
print(registry)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](../../../api.md) before writing a call.

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from scalar_sdk import APIStatusError

try:
    registry = client.registry.list_all_api_documents()
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](../../../README.md) — full feature tour: client options, request options, retries and timeouts, logging.
- [api.md](../../../api.md) — complete catalogue of every operation with request and response types.
