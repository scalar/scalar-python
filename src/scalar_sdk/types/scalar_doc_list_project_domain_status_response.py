# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ScalarDocListProjectDomainStatusResponse", "Expected"]


class Expected(BaseModel):
    type: Literal["CNAME"]

    target: str


class ScalarDocListProjectDomainStatusResponse(BaseModel):
    domain: Optional[str] = None

    status: Literal["verified", "pending", "misconfigured"]

    expected: Optional[Expected] = None

    found: List[str]
