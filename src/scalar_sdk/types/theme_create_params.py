# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ThemeCreateParams"]


class ThemeCreateParams(TypedDict, total=False):
    name: Required[str]

    description: str

    slug: Required[str]

    document: Required[str]
