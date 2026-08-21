# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .shared.timestamp import Timestamp

__all__ = ["AuthenticationListCurrentUserResponse", "Team"]


class Team(BaseModel):
    uid: Nanoid

    name: str

    image_uri: Optional[str] = FieldInfo(alias="imageUri", default=None)


class AuthenticationListCurrentUserResponse(BaseModel):
    uid: Nanoid

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    email: str

    theme: Optional[str] = None

    active_team_id: Optional[str] = FieldInfo(alias="activeTeamId", default=None)

    has_github: bool = FieldInfo(alias="hasGithub")

    teams: List[Team]
