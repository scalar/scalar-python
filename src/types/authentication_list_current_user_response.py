# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthenticationListCurrentUserResponse", "TeamSummary"]


class TeamSummary(BaseModel):

    uid: str

    name: str

    image_uri: Optional[str] = FieldInfo(alias="imageUri", default=None)



class AuthenticationListCurrentUserResponse(BaseModel):

    uid: str

    created_at: int = FieldInfo(alias="createdAt")

    updated_at: int = FieldInfo(alias="updatedAt")

    email: str

    theme: Optional[str] = None

    active_team_id: Optional[str] = FieldInfo(alias="activeTeamId", default=None)

    has_github: bool = FieldInfo(alias="hasGithub")

    teams: List[TeamSummary]
