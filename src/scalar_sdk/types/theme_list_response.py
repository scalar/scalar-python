# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .slug import Slug

__all__ = ["ThemeListResponse", "ThemeListResponseItem"]


class ThemeListResponseItem(BaseModel):
    uid: Nanoid

    name: str

    description: str

    slug: Slug


ThemeListResponse: TypeAlias = List[ThemeListResponseItem]
