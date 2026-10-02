# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

from ...slug import Slug

__all__ = ["InstallationUpdateParams"]


class InstallationUpdateParams(TypedDict, total=False):
    id: Required[str]

    name: str

    slug: Slug

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    login_portal_uid: Annotated[Optional[str], PropertyInfo(alias="loginPortalUid")]

    document_auth: Annotated[Dict[str, object], PropertyInfo(alias="documentAuth")]

    mcp_version: Annotated[Optional[str], PropertyInfo(alias="mcpVersion")]
