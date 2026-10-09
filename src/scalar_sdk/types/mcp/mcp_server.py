# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..slug import Slug

__all__ = ["McpServer"]


class McpServer(BaseModel):
    id: str

    name: str

    slug: Slug

    auto_add_operations: bool = FieldInfo(alias="autoAddOperations")

    created_at: str = FieldInfo(alias="createdAt")

    updated_at: str = FieldInfo(alias="updatedAt")
