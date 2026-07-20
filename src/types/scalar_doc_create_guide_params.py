# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .slug import Slug

__all__ = ["ScalarDocCreateGuideParams"]


class ScalarDocCreateGuideParams(TypedDict, total=False):

    name: Required[str]

    slug: Slug

    is_private: Required[Annotated[bool, PropertyInfo(alias="isPrivate")]]

    allowed_users: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedUsers")]]

    allowed_domains: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedDomains")]]
