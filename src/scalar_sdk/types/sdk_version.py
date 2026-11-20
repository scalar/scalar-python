# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.timestamp import Timestamp

__all__ = ["SdkVersion"]


class SdkVersion(BaseModel):
    version: str

    created_at: Timestamp = FieldInfo(alias="createdAt")

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
