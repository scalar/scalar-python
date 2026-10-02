# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .slug import Slug
from .shared.namespace import Namespace
from .managed_schema_version import ManagedSchemaVersion

__all__ = ["Schema"]


class Schema(BaseModel):
    uid: Nanoid

    title: str

    description: str

    slug: Slug

    namespace: Namespace

    is_private: bool = FieldInfo(alias="isPrivate")

    versions: List[ManagedSchemaVersion]
