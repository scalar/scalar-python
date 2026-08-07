# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

from .slug import Slug

__all__ = ["ThemeListResponse", "Theme"]


class Theme(BaseModel):
    uid: str

    name: str

    description: str

    slug: Slug


ThemeListResponse: TypeAlias = List[Theme]
