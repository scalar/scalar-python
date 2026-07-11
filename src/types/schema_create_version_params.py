# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .version import Version

__all__ = ["SchemaCreateVersionParams"]


class SchemaCreateVersionParams(TypedDict, total=False):

    version: Required[Version]

    document: Required[str]
