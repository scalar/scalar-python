# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Annotated
from typing_extensions import Required, TypedDict
from ..._utils import PropertyInfo

__all__ = ["AccessGroupCreateSchemaParams"]


class AccessGroupCreateSchemaParams(TypedDict, total=False):

    access_group_slug: Required[Annotated[str, PropertyInfo(alias="accessGroupSlug")]]
