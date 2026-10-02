# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

from .slug import Slug
from .shared.nanoid import Nanoid

__all__ = ["SdkUpdateParams"]


class SdkUpdateParams(TypedDict, total=False):
    title: str

    slug: Slug

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    config: str

    api_uid: Annotated[Optional[Nanoid], PropertyInfo(alias="apiUid")]

    api_version: Annotated[Optional[str], PropertyInfo(alias="apiVersion")]
