# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .role import Role

__all__ = ["MemberUpdateParams"]


class MemberUpdateParams(TypedDict, total=False):
    role: Required[Role]
