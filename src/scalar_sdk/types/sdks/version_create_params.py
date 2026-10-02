# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VersionCreateParams"]


class VersionCreateParams(TypedDict, total=False):
    version: Required[str]

    api_version: Required[Annotated[str, PropertyInfo(alias="apiVersion")]]
