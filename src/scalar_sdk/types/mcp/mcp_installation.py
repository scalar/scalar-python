# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..slug import Slug

__all__ = ["McpInstallation"]


class McpInstallation(BaseModel):
    id: str

    mcp_server_id: str = FieldInfo(alias="mcpServerId")

    name: str

    slug: Slug

    is_private: bool = FieldInfo(alias="isPrivate")

    access_groups: List[str] = FieldInfo(alias="accessGroups")

    login_portal_uid: Optional[str] = FieldInfo(alias="loginPortalUid", default=None)

    mcp_version: Optional[str] = FieldInfo(alias="mcpVersion", default=None)

    pii_redaction_enabled: bool = FieldInfo(alias="piiRedactionEnabled")

    credential_redaction_enabled: bool = FieldInfo(alias="credentialRedactionEnabled")
