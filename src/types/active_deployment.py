# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel
from .timestamp import Timestamp

__all__ = ["ActiveDeployment"]


class ActiveDeployment(BaseModel):

    uid: str

    domain: str

    publishedAt: Timestamp
