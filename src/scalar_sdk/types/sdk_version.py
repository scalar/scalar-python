# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .version import Version
from .shared.timestamp import Timestamp

__all__ = ["SdkVersion"]


class SdkVersion(BaseModel):
    version: Version

    api_version: Version = FieldInfo(alias="apiVersion")

    status: Literal["draft", "published"]

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

    published_at: Optional[Timestamp] = FieldInfo(alias="publishedAt", default=None)

    created_at: Optional[Timestamp] = FieldInfo(alias="createdAt", default=None)
