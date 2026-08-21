# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .login_portal_email_param import LoginPortalEmailParam
from .login_portal_page_param import LoginPortalPageParam

__all__ = ["LoginPortalCreateParams"]


class LoginPortalCreateParams(TypedDict, total=False):
    title: Required[str]

    slug: Required[str]

    email: Required[LoginPortalEmailParam]

    page: Required[LoginPortalPageParam]
