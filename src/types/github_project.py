# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel
from .nanoid import Nanoid
from .timestamp import Timestamp
from .active_deployment import ActiveDeployment
from .slug import Slug
from .github_project_repository import GithubProjectRepository

__all__ = ["GithubProject"]


class GithubProject(BaseModel):

    uid: Nanoid

    createdAt: Timestamp

    updatedAt: Timestamp

    name: str

    activeDeployment: Optional[ActiveDeployment] = None

    lastPublished: Optional[Timestamp] = None

    lastPublishedUid: Optional[str] = None

    loginPortalUid: str

    activeThemeId: str

    typesenseId: Optional[float] = None

    isPrivate: bool

    agentEnabled: bool

    accessGroups: str

    slug: Slug

    publishStatus: str

    publishMessage: str

    repository: Optional[GithubProjectRepository] = None
