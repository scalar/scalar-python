# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .mcp_installation_list_item import McpInstallationListItem

__all__ = ["InstallationListResponse"]

InstallationListResponse: TypeAlias = List[McpInstallationListItem]
