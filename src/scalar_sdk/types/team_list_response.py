# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .slug import Slug

__all__ = ["TeamListResponse", "TeamListResponseItem"]


class TeamListResponseItem(BaseModel):
    uid: Nanoid

    name: str

    image_uri: Optional[str] = FieldInfo(alias="imageUri", default=None)

    slug: Slug

    theme: str


TeamListResponse: TypeAlias = List[TeamListResponseItem]
