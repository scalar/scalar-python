# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["RuleCreateRulesetParams"]


class RuleCreateRulesetParams(TypedDict, total=False):

    title: Required[str]

    description: str

    slug: Required[str]

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    document: Required[str]
