# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScalarDocUpdateProjectConfigParams"]


class ScalarDocUpdateProjectConfigParams(TypedDict, total=False):
    content: Required[str]

    ref: str

    base_token: Annotated[str, PropertyInfo(alias="baseToken")]

    message: str

    path: str
