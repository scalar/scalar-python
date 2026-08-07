# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LoginPortalPage"]


class LoginPortalPage(BaseModel):
    title: str

    description: str

    head: str

    script: str

    theme: str

    company_name: str = FieldInfo(alias="companyName")

    logo: str

    logo_url: str = FieldInfo(alias="logoURL")

    favicon: str

    terms_link: str = FieldInfo(alias="termsLink")

    privacy_link: str = FieldInfo(alias="privacyLink")

    form_title: str = FieldInfo(alias="formTitle")

    form_description: str = FieldInfo(alias="formDescription")

    form_image: str = FieldInfo(alias="formImage")
