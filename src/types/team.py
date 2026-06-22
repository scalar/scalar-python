# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel
from .nanoid import Nanoid
from .team_name import TeamName
from .team_image import TeamImage
from .slug import Slug

__all__ = ["Team"]


class Team(BaseModel):

    uid: Nanoid

    name: TeamName

    imageUri: Optional[TeamImage] = None

    slug: Slug

    theme: str
