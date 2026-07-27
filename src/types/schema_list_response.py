# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .slug import Slug
from .version import Version

__all__ = ["SchemaListResponse", "Schema", "Version"]

class Version(BaseModel):

    uid: str

    created_at: int = FieldInfo(alias="createdAt")

    updated_at: int = FieldInfo(alias="updatedAt")

    version: Version

class Schema(BaseModel):

    uid: str

    title: str

    description: str

    slug: Slug

    namespace: str

    is_private: bool = FieldInfo(alias="isPrivate")

    versions: List[Version]



SchemaListResponse: TypeAlias = List[Schema]
