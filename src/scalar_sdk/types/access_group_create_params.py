# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

from .access_group_name import AccessGroupName
from .slug import Slug

__all__ = ["AccessGroupCreateParams"]


class AccessGroupCreateParams(TypedDict, total=False):
    name: AccessGroupName

    slug: Slug

    allowed_domains: Annotated[str, PropertyInfo(alias="allowedDomains")]
