# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel

__all__ = ["LoginPortalPage"]


class LoginPortalPage(BaseModel):

    title: str

    description: str

    head: str

    script: str

    theme: str

    companyName: str

    logo: str

    logoURL: str

    favicon: str

    termsLink: str

    privacyLink: str

    formTitle: str

    formDescription: str

    formImage: str
