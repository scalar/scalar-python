# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LoginPortalEmail"]


class LoginPortalEmail(TypedDict, total=False):

    logo: Required[str]

    logo_size: Required[Annotated[str, PropertyInfo(alias="logoSize")]]

    button_text: Required[Annotated[str, PropertyInfo(alias="buttonText")]]

    message: Required[str]

    title: Required[str]

    main_color: Required[Annotated[str, PropertyInfo(alias="mainColor")]]

    main_background: Required[Annotated[str, PropertyInfo(alias="mainBackground")]]

    card_color: Required[Annotated[str, PropertyInfo(alias="cardColor")]]

    card_background: Required[Annotated[str, PropertyInfo(alias="cardBackground")]]

    button_color: Required[Annotated[str, PropertyInfo(alias="buttonColor")]]

    button_background: Required[Annotated[str, PropertyInfo(alias="buttonBackground")]]
