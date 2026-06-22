# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel
from .nanoid import Nanoid
from .timestamp import Timestamp
from .version import Version

__all__ = ["ManagedSchemaVersion"]


class ManagedSchemaVersion(BaseModel):

    uid: Nanoid

    createdAt: Timestamp

    updatedAt: Timestamp

    version: Version
