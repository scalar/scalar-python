# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

from .nanoid import Nanoid

__all__ = ["UID"]


class UID(BaseModel):
    uid: Nanoid
