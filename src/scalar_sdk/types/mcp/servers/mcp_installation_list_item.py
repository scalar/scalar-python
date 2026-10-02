# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from ...slug import Slug

__all__ = ["McpInstallationListItem"]


class McpInstallationListItem(BaseModel):
    id: str

    name: str

    slug: Slug

    is_private: bool = FieldInfo(alias="isPrivate")

    mcp_version: Optional[str] = FieldInfo(alias="mcpVersion", default=None)
