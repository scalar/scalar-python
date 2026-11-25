# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

from .shared.nanoid import Nanoid
from .slug import Slug

__all__ = ["SdkCreateParams"]


class SdkCreateParams(TypedDict, total=False):
    api_uid: Required[Annotated[Nanoid, PropertyInfo(alias="apiUid")]]

    languages: List[
        Literal[
            "typescript",
            "python",
            "cli",
            "csharp",
            "java",
            "ruby",
            "php",
            "go",
            "rust",
            "kotlin",
            "swift",
            "cpp",
            "dart",
        ]
    ]
    """Languages to create. Defaults to the targets declared by config."""

    title: str

    slug: Slug

    class_name: Annotated[str, PropertyInfo(alias="className")]

    config: str
