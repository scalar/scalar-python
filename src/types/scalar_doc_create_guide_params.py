# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Annotated, List
from typing_extensions import Required, TypedDict
from .._utils import PropertyInfo

__all__ = ["ScalarDocCreateGuideParams"]


class ScalarDocCreateGuideParams(TypedDict, total=False):

    name: Required[str]

    slug: str

    is_private: Required[Annotated[bool, PropertyInfo(alias="isPrivate")]]

    allowed_users: Required[Annotated[List[str], PropertyInfo(alias="allowedUsers")]]

    allowed_domains: Required[Annotated[List[str], PropertyInfo(alias="allowedDomains")]]
