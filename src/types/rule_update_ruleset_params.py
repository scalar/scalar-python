# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["RuleUpdateRulesetParams"]


class RuleUpdateRulesetParams(TypedDict, total=False):
    path_namespace: Required[Annotated[str, PropertyInfo(alias="namespace")]]

    body_namespace: Annotated[str, PropertyInfo(alias="namespace")]

    body_slug: Annotated[str, PropertyInfo(alias="slug")]

    title: str

    description: str

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]
