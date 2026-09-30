# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

from ..shared.nanoid import Nanoid

__all__ = ["VersionCreateResponse"]


class VersionCreateResponse(BaseModel):
    uid: Nanoid
