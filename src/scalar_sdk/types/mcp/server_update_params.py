# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

from ..slug import Slug

__all__ = ["ServerUpdateParams"]


class ServerUpdateParams(TypedDict, total=False):
    name: str

    slug: Slug

    auto_add_operations: Annotated[bool, PropertyInfo(alias="autoAddOperations")]

    operations: SequenceNotStr[str]

    docs_pages: Annotated[SequenceNotStr[str], PropertyInfo(alias="docsPages")]
