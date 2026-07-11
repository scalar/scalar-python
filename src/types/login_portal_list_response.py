# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

from .slug import Slug

__all__ = ["LoginPortalListResponse", "LoginPortal"]

class LoginPortal(BaseModel):

    uid: str

    title: str

    slug: Slug



LoginPortalListResponse: TypeAlias = List[LoginPortal]
