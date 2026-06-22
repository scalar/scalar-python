# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .nanoid import Nanoid
from .version import Version

__all__ = ["ManagedDocVersion"]


class ManagedDocVersion(BaseModel):

    uid: Nanoid

    createdAt: float

    version: Version

    upgraded: bool

    embedStatus: Optional[Literal["complete", "failed"]] = None

    tags: List[str]

    tools: Optional[List[object]] = None

    yamlSha: Optional[str] = None

    jsonSha: Optional[str] = None

    versionSha: Optional[str] = None
