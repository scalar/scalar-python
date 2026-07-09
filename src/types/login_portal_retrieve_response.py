# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import TypeAlias
from .._models import BaseModel
from .login_portal_email import LoginPortalEmail
from .login_portal_page import LoginPortalPage

__all__ = ["LoginPortalRetrieveResponse", "LoginPortalRetrieveResponse"]

class LoginPortalRetrieveResponse(BaseModel):

    uid: str

    title: str

    slug: str

    email: LoginPortalEmail

    page: LoginPortalPage



LoginPortalRetrieveResponse: TypeAlias = LoginPortalRetrieveResponse
