# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LoginPortalEmail"]


class LoginPortalEmail(BaseModel):

    logo: str

    logo_size: str = FieldInfo(alias="logoSize")

    button_text: str = FieldInfo(alias="buttonText")

    message: str

    title: str

    main_color: str = FieldInfo(alias="mainColor")

    main_background: str = FieldInfo(alias="mainBackground")

    card_color: str = FieldInfo(alias="cardColor")

    card_background: str = FieldInfo(alias="cardBackground")

    button_color: str = FieldInfo(alias="buttonColor")

    button_background: str = FieldInfo(alias="buttonBackground")
