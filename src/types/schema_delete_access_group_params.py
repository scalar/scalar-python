# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict
from .slug import Slug
from .._utils import PropertyInfo

__all__ = ["SchemaDeleteAccessGroupParams"]


class SchemaDeleteAccessGroupParams(TypedDict, total=False):

    access_group_slug: Required[Annotated[Slug, PropertyInfo(alias="accessGroupSlug")]]
