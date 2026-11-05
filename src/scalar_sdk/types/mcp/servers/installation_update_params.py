# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

from ...slug import Slug

__all__ = ["InstallationUpdateParams"]


class InstallationUpdateParams(TypedDict, total=False):
    id: Required[str]

    name: str

    slug: Slug
    """The environment’s current slug. An environment cannot be renamed, so any other slug is refused."""

    mcp_version: Annotated[Optional[str], PropertyInfo(alias="mcpVersion")]
