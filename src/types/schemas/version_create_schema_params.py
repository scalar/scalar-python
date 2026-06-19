# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VersionCreateSchemaParams"]


class VersionCreateSchemaParams(TypedDict, total=False):

    version: Required[str]

    document: Required[str]
