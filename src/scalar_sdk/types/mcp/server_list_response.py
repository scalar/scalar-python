# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .mcp_server import McpServer

__all__ = ["ServerListResponse"]

ServerListResponse: TypeAlias = List[McpServer]
