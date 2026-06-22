# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel
from .nanoid import Nanoid
from .team_name import TeamName
from .team_image import TeamImage

__all__ = ["TeamSummary"]


class TeamSummary(BaseModel):

    uid: Nanoid

    name: TeamName

    imageUri: Optional[TeamImage] = None
