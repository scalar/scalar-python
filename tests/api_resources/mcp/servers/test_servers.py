# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestServers:
    @smoke_case("mcp.servers.list:single", operation="list", path="/v1/mcp/servers")
    def test_method_list(self) -> None:
        server = client.mcp.servers.list()

    @smoke_case("mcp.servers.create:required", operation="create", path="/v1/mcp/servers")
    def test_method_create(self) -> None:
        server = client.mcp.servers.create(
            name="Acme MCP",
        )

    @smoke_case("mcp.servers.create:all", operation="create", path="/v1/mcp/servers")
    def test_method_create_with_all_params(self) -> None:
        server = client.mcp.servers.create(
            name="Acme MCP",
            slug="acme-mcp",
            version_uids=["VakgbKJ5m9gl0JDMbcJqL"],
            project_uids=["PakgbKJ5m9gl0JDMbcJqL"],
        )

    @smoke_case("mcp.servers.retrieve:single", operation="retrieve", path="/v1/mcp/servers/{id}")
    def test_method_retrieve(self) -> None:
        server = client.mcp.servers.retrieve(
            id="42",
        )

    @smoke_case("mcp.servers.update:required", operation="update", path="/v1/mcp/servers/{id}")
    def test_method_update(self) -> None:
        server = client.mcp.servers.update(
            id="42",
        )

    @smoke_case("mcp.servers.update:all", operation="update", path="/v1/mcp/servers/{id}")
    def test_method_update_with_all_params(self) -> None:
        server = client.mcp.servers.update(
            id="42",
            name="Acme MCP",
            slug="acme-mcp",
            operations=["42"],
            docs_pages=["getting-started"],
        )

    @smoke_case("mcp.servers.delete:single", operation="delete", path="/v1/mcp/servers/{id}")
    def test_method_delete(self) -> None:
        server = client.mcp.servers.delete(
            id="42",
        )
