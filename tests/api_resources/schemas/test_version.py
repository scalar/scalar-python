# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVersion:
    @smoke_case(
        "schemas.version.retrieve:single", operation="retrieve", path="/v1/schemas/{namespace}/{slug}/version/{semver}"
    )
    def test_method_retrieve(self) -> None:
        version = client.schemas.version.retrieve(
            namespace="acme",
            slug="customer",
            semver="1.2.0",
        )

    @smoke_case(
        "schemas.version.delete:single", operation="delete", path="/v1/schemas/{namespace}/{slug}/version/{semver}"
    )
    def test_method_delete(self) -> None:
        version = client.schemas.version.delete(
            namespace="acme",
            slug="customer",
            semver="1.2.0",
        )

    @smoke_case("schemas.version.create:required", operation="create", path="/v1/schemas/{namespace}/{slug}/version")
    def test_method_create(self) -> None:
        version = client.schemas.version.create(
            namespace="acme",
            slug="customer",
            version="1.2.0",
            document='{"type":"object","properties":{"name":{"type":"string","examples":["Acme"]}}}',
        )

    @smoke_case("schemas.version.create:all", operation="create", path="/v1/schemas/{namespace}/{slug}/version")
    def test_method_create_with_all_params(self) -> None:
        version = client.schemas.version.create(
            namespace="acme",
            slug="customer",
            version="1.2.0",
            document='{"type":"object","properties":{"name":{"type":"string","examples":["Acme"]}}}',
            force=False,
        )
