# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthenticationExchangePersonalTokenParams"]


class AuthenticationExchangePersonalTokenParams(TypedDict, total=False):
    personal_token: Required[Annotated[str, PropertyInfo(alias="personalToken")]]
