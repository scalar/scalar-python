# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .email_domain import EmailDomain

__all__ = ["DomainDeleteParams"]


class DomainDeleteParams(TypedDict, total=False):
    domain: Required[EmailDomain]
