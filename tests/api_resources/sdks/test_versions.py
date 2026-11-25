# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVersions:
    @smoke_case("sdks.versions.create:required", operation="create", path="/v1/sdks/{uid}/versions")
    def test_method_create(self) -> None:
        version = client.sdks.versions.create(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            version="1.2.0",
        )

    @smoke_case("sdks.versions.create:all", operation="create", path="/v1/sdks/{uid}/versions")
    def test_method_create_with_all_params(self) -> None:
        version = client.sdks.versions.create(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            version="1.2.0",
            api_version={},
        )

    @smoke_case("sdks.versions.delete:single", operation="delete", path="/v1/sdks/{uid}/versions/{version}")
    def test_method_delete(self) -> None:
        version = client.sdks.versions.delete(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            version="1.2.0",
        )
