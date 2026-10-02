# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .team_member import TeamMember
from .team_invite import TeamInvite

__all__ = ["MemberListResponse"]


class MemberListResponse(BaseModel):
    members: List[TeamMember]

    pending_invites: List[TeamInvite] = FieldInfo(alias="pendingInvites")
