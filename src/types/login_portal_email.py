# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel

__all__ = ["LoginPortalEmail"]


class LoginPortalEmail(BaseModel):

    logo: str

    logoSize: str

    buttonText: str

    message: str

    title: str

    mainColor: str

    mainBackground: str

    cardColor: str

    cardBackground: str

    buttonColor: str

    buttonBackground: str
