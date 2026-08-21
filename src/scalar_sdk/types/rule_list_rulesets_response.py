# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .slug import Slug
from .shared.namespace import Namespace

__all__ = ["RuleListRulesetsResponse", "RuleListRulesetsResponseItem"]


class RuleListRulesetsResponseItem(BaseModel):
    uid: Nanoid

    title: str

    description: str

    slug: Slug

    namespace: Namespace

    is_private: bool = FieldInfo(alias="isPrivate")


RuleListRulesetsResponse: TypeAlias = List[RuleListRulesetsResponseItem]
