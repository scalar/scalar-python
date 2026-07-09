# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias
from .._models import BaseModel
from .slug import Slug

__all__ = ["TeamListResponse", "Team"]

class Team(BaseModel):

    uid: str

    name: str

    imageUri: Optional[str] = None

    slug: Slug

    theme: str



TeamListResponse: TypeAlias = List[Team]
