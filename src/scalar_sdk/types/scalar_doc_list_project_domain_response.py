# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScalarDocListProjectDomainResponse"]


class ScalarDocListProjectDomainResponse(BaseModel):
    scalar_domain: Optional[str] = FieldInfo(alias="scalarDomain", default=None)

    custom_domain: Optional[str] = FieldInfo(alias="customDomain", default=None)
