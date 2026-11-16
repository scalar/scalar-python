# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestSchemas:
    @smoke_case("schemas.list:single", operation="list", path="/v1/schemas/{namespace}")
    def test_method_list(self) -> None:
        schema = client.schemas.list(
            namespace="acme",
        )

    @smoke_case("schemas.create:required", operation="create", path="/v1/schemas/{namespace}")
    def test_method_create(self) -> None:
        schema = client.schemas.create(
            namespace="acme",
            title="Customer",
            version="1.2.0",
            slug="customer",
            document='{"type":"object","properties":{"name":{"type":"string","examples":["Acme"]}}}',
        )

    @smoke_case("schemas.create:all", operation="create", path="/v1/schemas/{namespace}")
    def test_method_create_with_all_params(self) -> None:
        schema = client.schemas.create(
            namespace="acme",
            title="Customer",
            description="API for managing Acme products and orders.",
            version="1.2.0",
            slug="customer",
            is_private=False,
            document='{"type":"object","properties":{"name":{"type":"string","examples":["Acme"]}}}',
        )

    @smoke_case("schemas.update:required", operation="update", path="/v1/schemas/{namespace}/{slug}")
    def test_method_update(self) -> None:
        schema = client.schemas.update(
            namespace="acme",
            slug="customer",
        )

    @smoke_case("schemas.update:all", operation="update", path="/v1/schemas/{namespace}/{slug}")
    def test_method_update_with_all_params(self) -> None:
        schema = client.schemas.update(
            namespace="acme",
            slug="customer",
            title="Customer",
            description="API for managing Acme products and orders.",
            is_private=False,
        )

    @smoke_case("schemas.delete:single", operation="delete", path="/v1/schemas/{namespace}/{slug}")
    def test_method_delete(self) -> None:
        schema = client.schemas.delete(
            namespace="acme",
            slug="customer",
        )
