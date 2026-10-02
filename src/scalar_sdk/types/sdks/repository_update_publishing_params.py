# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

from ..shared.nanoid import Nanoid

__all__ = ["RepositoryUpdatePublishingParams"]


class RepositoryUpdatePublishingParams(TypedDict, total=False):
    uid: Required[Nanoid]

    publish_on_merge: Required[Annotated[bool, PropertyInfo(alias="publishOnMerge")]]

    auth_method: Annotated[Literal["oidc", "access-token"], PropertyInfo(alias="authMethod")]

    access: Literal["public", "restricted"]

    tag: str
