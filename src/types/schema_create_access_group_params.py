# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .slug import Slug

__all__ = ["SchemaCreateAccessGroupParams"]


class SchemaCreateAccessGroupParams(TypedDict, total=False):

    access_group_slug: Required[Annotated[Slug, PropertyInfo(alias="accessGroupSlug")]]
