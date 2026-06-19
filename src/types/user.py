# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union

from .._models import BaseModel
from .nanoid import Nanoid
from .timestamp import Timestamp
from .email import Email
from .team_summary import TeamSummary

__all__ = ["User"]


class User(BaseModel):

    uid: Nanoid

    createdAt: Timestamp

    updatedAt: Timestamp

    email: Email

    theme: Optional[str] = None

    activeTeamId: Optional[Union[str, None]] = None

    hasGithub: bool

    teams: List[TeamSummary]
