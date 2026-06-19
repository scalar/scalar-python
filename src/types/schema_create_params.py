# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Annotated
from typing_extensions import Required, TypedDict
from .._utils import PropertyInfo

__all__ = ["SchemaCreateParams"]


class SchemaCreateParams(TypedDict, total=False):

    title: Required[str]

    description: str

    version: Required[str]

    slug: Required[str]

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    document: Required[str]
