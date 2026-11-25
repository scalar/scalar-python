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
