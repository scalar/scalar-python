# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestNamespaces:
    @smoke_case("namespaces.list:single", operation="list", path="/v1/namespaces")
    def test_method_list(self) -> None:
        namespace = client.namespaces.list()
