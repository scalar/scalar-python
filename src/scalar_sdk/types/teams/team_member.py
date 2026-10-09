# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.nanoid import Nanoid
from .role import Role

__all__ = ["TeamMember"]


class TeamMember(BaseModel):
    uid: Nanoid

    role: Role

    display_name: str = FieldInfo(alias="displayName")

    image_uri: Optional[str] = FieldInfo(alias="imageUri", default=None)
