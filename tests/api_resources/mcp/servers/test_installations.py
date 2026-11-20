# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestInstallations:
    @smoke_case("mcp.servers.installations.list:single", operation="list", path="/v1/mcp/servers/{id}/installations")
    def test_method_list(self) -> None:
        installation = client.mcp.servers.installations.list(
            id="42",
        )

    @smoke_case(
        "mcp.servers.installations.retrieve:single",
        operation="retrieve",
        path="/v1/mcp/servers/{id}/installations/{installationId}",
    )
    def test_method_retrieve(self) -> None:
        installation = client.mcp.servers.installations.retrieve(
            id="42",
            installation_id="84",
        )

    @smoke_case(
        "mcp.servers.installations.update:required",
        operation="update",
        path="/v1/mcp/servers/{id}/installations/{installationId}",
    )
    def test_method_update(self) -> None:
        installation = client.mcp.servers.installations.update(
            id="42",
            installation_id="84",
        )

    @smoke_case(
        "mcp.servers.installations.update:all",
        operation="update",
        path="/v1/mcp/servers/{id}/installations/{installationId}",
    )
    def test_method_update_with_all_params(self) -> None:
        installation = client.mcp.servers.installations.update(
            id="42",
            installation_id="84",
            name="Acme MCP",
            slug="staging",
            mcp_version="1.2.0",
        )

    @smoke_case(
        "mcp.servers.installations.delete:single",
        operation="delete",
        path="/v1/mcp/servers/{id}/installations/{installationId}",
    )
    def test_method_delete(self) -> None:
        installation = client.mcp.servers.installations.delete(
            id="42",
            installation_id="84",
        )

    @smoke_case(
        "mcp.servers.installations.createAccessGroup:single",
        operation="createAccessGroup",
        path="/v1/mcp/servers/{id}/installations/{installationId}/access-group",
    )
    def test_method_create_access_group(self) -> None:
        installation = client.mcp.servers.installations.create_access_group(
            id="42",
            installation_id="84",
            access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
        )

    @smoke_case(
        "mcp.servers.installations.deleteAccessGroup:single",
        operation="deleteAccessGroup",
        path="/v1/mcp/servers/{id}/installations/{installationId}/access-group",
    )
    def test_method_delete_access_group(self) -> None:
        installation = client.mcp.servers.installations.delete_access_group(
            id="42",
            installation_id="84",
            access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
        )
