# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel

__all__ = ["GithubProjectRepository"]


class GithubProjectRepository(BaseModel):

    linkedBy: str

    id: float

    name: str

    configPath: str

    branch: str

    publishOnMerge: bool

    publishPreviews: bool

    prComments: bool

    expired: bool
