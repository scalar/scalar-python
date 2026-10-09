# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

from .mcp_server import McpServer
from .mcp_installation import McpInstallation

__all__ = ["ServerCreateResponse"]


class ServerCreateResponse(BaseModel):
    server: McpServer

    installation: McpInstallation
