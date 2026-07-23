# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["LoginPortalPageParam"]


class LoginPortalPageParam(TypedDict, total=False):

    title: Required[str]

    description: Required[str]

    head: Required[str]

    script: Required[str]

    theme: Required[str]

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    logo: Required[str]

    logo_url: Required[Annotated[str, PropertyInfo(alias="logoURL")]]

    favicon: Required[str]

    terms_link: Required[Annotated[str, PropertyInfo(alias="termsLink")]]

    privacy_link: Required[Annotated[str, PropertyInfo(alias="privacyLink")]]

    form_title: Required[Annotated[str, PropertyInfo(alias="formTitle")]]

    form_description: Required[Annotated[str, PropertyInfo(alias="formDescription")]]

    form_image: Required[Annotated[str, PropertyInfo(alias="formImage")]]
