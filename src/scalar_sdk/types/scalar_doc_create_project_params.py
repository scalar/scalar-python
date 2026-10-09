# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

from .slug import Slug

__all__ = ["ScalarDocCreateProjectParams", "GithubRepository", "BitbucketRepository"]


class ScalarDocCreateProjectParams(TypedDict, total=False):
    name: Required[str]

    slug: Slug

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    blank: bool

    provider: Required[Literal["forgejo", "github", "bitbucket"]]

    github_repository: Annotated[GithubRepository, PropertyInfo(alias="githubRepository")]

    bitbucket_repository: Annotated[BitbucketRepository, PropertyInfo(alias="bitbucketRepository")]


class BitbucketRepository(TypedDict, total=False):
    workspace_uuid: Required[Annotated[str, PropertyInfo(alias="workspaceUuid")]]

    repo_uuid: Required[Annotated[str, PropertyInfo(alias="repoUuid")]]


class GithubRepository(TypedDict, total=False):
    installation_id: Required[Annotated[int, PropertyInfo(alias="installationId")]]

    repo_id: Required[Annotated[int, PropertyInfo(alias="repoId")]]
