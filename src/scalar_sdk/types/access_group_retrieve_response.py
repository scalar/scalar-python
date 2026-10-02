# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .access_group_name import AccessGroupName
from .slug import Slug

__all__ = ["AccessGroupRetrieveResponse"]


class AccessGroupRetrieveResponse(BaseModel):
    uid: Nanoid

    name: AccessGroupName

    slug: Slug

    allowed_domains: str = FieldInfo(alias="allowedDomains")

    allowed_emails: str = FieldInfo(alias="allowedEmails")
