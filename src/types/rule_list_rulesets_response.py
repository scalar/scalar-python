# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .slug import Slug

__all__ = ["RuleListRulesetsResponse", "Rule"]


class Rule(BaseModel):
    uid: str

    title: str

    description: str

    slug: Slug

    namespace: str

    is_private: bool = FieldInfo(alias="isPrivate")


RuleListRulesetsResponse: TypeAlias = List[Rule]
