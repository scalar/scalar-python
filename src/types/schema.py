# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel
from .nanoid import Nanoid
from .slug import Slug
from .namespace import Namespace
from .managed_schema_version import ManagedSchemaVersion

__all__ = ["Schema"]


class Schema(BaseModel):

    uid: Nanoid

    title: str

    description: str

    slug: Slug

    namespace: Namespace

    isPrivate: bool

    versions: List[ManagedSchemaVersion]
