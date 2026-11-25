# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.nanoid import Nanoid
from ..slug import Slug
from ..shared.namespace import Namespace
from ..shared.timestamp import Timestamp

__all__ = ["McpServer"]


class McpServer(BaseModel):
    uid: Nanoid

    slug: Slug

    namespace: Namespace

    domain: Optional[str] = None

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    name: str
