# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Annotated
from typing_extensions import TypedDict
from .._utils import PropertyInfo

__all__ = ["RuleUpdateRulesetParams"]


class RuleUpdateRulesetParams(TypedDict, total=False):

    namespace: str

    slug: str

    title: str

    description: str

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]
