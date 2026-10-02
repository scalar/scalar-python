# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["RepositoryLinkResponse"]


class RepositoryLinkResponse(BaseModel):
    repo: str

    branch: str


RepositoryLinkResponse: TypeAlias = Optional[RepositoryLinkResponse]
