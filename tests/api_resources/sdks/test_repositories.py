# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestRepositories:
    @smoke_case("sdks.repositories.link:required", operation="link", path="/v1/sdks/{uid}/repositories")
    def test_method_link(self) -> None:
        repository = client.sdks.repositories.link(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            language="typescript",
            repository_id=123456789,
            base_branch="main",
        )

    @smoke_case("sdks.repositories.link:all", operation="link", path="/v1/sdks/{uid}/repositories")
    def test_method_link_with_all_params(self) -> None:
        repository = client.sdks.repositories.link(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            language="typescript",
            repository_id=123456789,
            base_branch="main",
            promotion="automatic",
            prerelease_type="beta",
        )

    @smoke_case("sdks.repositories.unlink:single", operation="unlink", path="/v1/sdks/{uid}/repositories/{language}")
    def test_method_unlink(self) -> None:
        repository = client.sdks.repositories.unlink(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            language="typescript",
        )

    @smoke_case(
        "sdks.repositories.updatePublishing:required",
        operation="updatePublishing",
        path="/v1/sdks/{uid}/repositories/{language}/publishing",
    )
    def test_method_update_publishing(self) -> None:
        repository = client.sdks.repositories.update_publishing(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            language="typescript",
            publish_on_merge=True,
        )

    @smoke_case(
        "sdks.repositories.updatePublishing:all",
        operation="updatePublishing",
        path="/v1/sdks/{uid}/repositories/{language}/publishing",
    )
    def test_method_update_publishing_with_all_params(self) -> None:
        repository = client.sdks.repositories.update_publishing(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            language="typescript",
            publish_on_merge=True,
            auth_method="oidc",
            access="public",
            tag="latest",
            artifact_id="scalar-galaxy",
            tap_repo="scalar/homebrew-tap",
            cask=True,
            replace_formula=False,
            registry="npm",
        )
