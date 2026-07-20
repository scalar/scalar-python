# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["SchemaUpdateParams"]


class SchemaUpdateParams(TypedDict, total=False):

    namespace: Required[str]

    title: str

    description: str

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]
