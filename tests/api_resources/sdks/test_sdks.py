# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestSdks:
    @smoke_case("sdks.list:required", operation="list", path="/v1/sdks")
    def test_method_list(self) -> None:
        sdk = client.sdks.list()

    @smoke_case("sdks.list:all", operation="list", path="/v1/sdks")
    def test_method_list_with_all_params(self) -> None:
        sdk = client.sdks.list(
            limit=20,
        )

    @smoke_case("sdks.create:required", operation="create", path="/v1/sdks")
    def test_method_create(self) -> None:
        sdk = client.sdks.create(
            api_uid="UakgbKJ5m9gl0JDMbcJqL",
            languages=["typescript"],
        )

    @smoke_case("sdks.create:all", operation="create", path="/v1/sdks")
    def test_method_create_with_all_params(self) -> None:
        sdk = client.sdks.create(
            api_uid="UakgbKJ5m9gl0JDMbcJqL",
            languages=["typescript"],
            title="Acme SDK",
            slug="acme-sdk",
            class_name="Acme",
            config='{"targets":{"typescript":{"packageName":"@acme/sdk"}}}',
        )

    @smoke_case("sdks.retrieve:single", operation="retrieve", path="/v1/sdks/{uid}")
    def test_method_retrieve(self) -> None:
        sdk = client.sdks.retrieve(
            uid="UakgbKJ5m9gl0JDMbcJqL",
        )

    @smoke_case("sdks.update:required", operation="update", path="/v1/sdks/{uid}")
    def test_method_update(self) -> None:
        sdk = client.sdks.update(
            uid="UakgbKJ5m9gl0JDMbcJqL",
        )

    @smoke_case("sdks.update:all", operation="update", path="/v1/sdks/{uid}")
    def test_method_update_with_all_params(self) -> None:
        sdk = client.sdks.update(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            title="Acme SDK",
            slug="acme-sdk",
            is_private=False,
            config='{"targets":{"typescript":{"packageName":"@acme/sdk"}}}',
            api_uid="UakgbKJ5m9gl0JDMbcJqL",
            api_version={},
        )

    @smoke_case("sdks.delete:single", operation="delete", path="/v1/sdks/{uid}")
    def test_method_delete(self) -> None:
        sdk = client.sdks.delete(
            uid="UakgbKJ5m9gl0JDMbcJqL",
        )

    @smoke_case("sdks.build:required", operation="build", path="/v1/sdks/{uid}/build")
    def test_method_build(self) -> None:
        sdk = client.sdks.build(
            uid="UakgbKJ5m9gl0JDMbcJqL",
        )

    @smoke_case("sdks.build:all", operation="build", path="/v1/sdks/{uid}/build")
    def test_method_build_with_all_params(self) -> None:
        sdk = client.sdks.build(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            version="1.2.0",
            custom_code_ref="scalar-next",
            languages=["typescript"],
        )
