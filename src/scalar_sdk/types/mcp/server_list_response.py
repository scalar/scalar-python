# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.nanoid import Nanoid
from ..slug import Slug
from ..shared.namespace import Namespace
from ..shared.timestamp import Timestamp

__all__ = ["ServerListResponse", "ServerListResponseItem", "ServerListResponseItemEnvironment"]


class ServerListResponseItemEnvironment(BaseModel):
    slug: str

    served: Optional[str] = None


class ServerListResponseItem(BaseModel):
    uid: Nanoid

    slug: Slug

    namespace: Namespace

    domain: Optional[str] = None

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    name: str

    environments: List[ServerListResponseItemEnvironment]


ServerListResponse: TypeAlias = List[ServerListResponseItem]
