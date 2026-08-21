# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .slug import Slug
from .shared.namespace import Namespace
from .shared.timestamp import Timestamp
from .version import Version

__all__ = ["SchemaListResponse", "SchemaListResponseItem", "SchemaListResponseItemVersion"]


class SchemaListResponseItemVersion(BaseModel):
    uid: Nanoid

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    version: Version


class SchemaListResponseItem(BaseModel):
    uid: Nanoid

    title: str

    description: str

    slug: Slug

    namespace: Namespace

    is_private: bool = FieldInfo(alias="isPrivate")

    versions: List[SchemaListResponseItemVersion]


SchemaListResponse: TypeAlias = List[SchemaListResponseItem]
