# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

from ..shared.nanoid import Nanoid
from .email import Email
from .role import Role

__all__ = ["TeamInvite"]


class TeamInvite(BaseModel):
    uid: Nanoid

    email: Email

    role: Role

    expires: Optional[float] = None
