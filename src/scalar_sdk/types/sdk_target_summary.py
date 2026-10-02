# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

from .slug import Slug

__all__ = ["SdkTargetSummary"]


class SdkTargetSummary(BaseModel):
    language: Literal[
        "typescript", "python", "cli", "csharp", "java", "ruby", "php", "go", "rust", "kotlin", "swift", "cpp", "dart"
    ]

    slug: Slug
