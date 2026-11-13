# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["SdkBuildParams"]


class SdkBuildParams(TypedDict, total=False):
    version: str

    custom_code_ref: Annotated[str, PropertyInfo(alias="customCodeRef")]

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
