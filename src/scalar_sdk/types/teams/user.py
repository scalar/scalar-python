# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.nanoid import Nanoid
from ..shared.timestamp import Timestamp
from .email import Email
from ..team_summary import TeamSummary

__all__ = ["User"]


class User(BaseModel):
    uid: Nanoid

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    email: Email

    theme: Optional[str] = None

    active_team_id: Optional[str] = FieldInfo(alias="activeTeamId", default=None)

    has_github: bool = FieldInfo(alias="hasGithub")

    teams: List[TeamSummary]
