# Scalar Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Registry`](#registry)
  - [List all API Documents](#list-all-api-documents)
  - [List API Documents in a namespace](#list-api-documents-in-a-namespace)
  - [Create API Document](#create-api-document)
  - [Update API Document metadata](#update-api-document-metadata)
  - [Delete API Document](#delete-api-document)
  - [Get API Document](#get-api-document)
  - [Update API Document version](#update-api-document-version)
  - [Delete API Document version](#delete-api-document-version)
  - [Get API Document version metadata](#get-api-document-version-metadata)
  - [Create API Document version](#create-api-document-version)
  - [Add access group](#add-access-group)
  - [Remove access group](#remove-access-group)
- [`Schemas`](#schemas)
  - [List all shared components](#list-all-shared-components)
  - [Create a shared component](#create-a-shared-component)
  - [Update shared component metadata](#update-shared-component-metadata)
  - [Delete a shared component](#delete-a-shared-component)
  - [`Schemas Version`](#schemas-version)
    - [Get a shared component document](#get-a-shared-component-document)
    - [Delete a shared component version](#delete-a-shared-component-version)
    - [Create a shared component version](#create-a-shared-component-version)
  - [`Schemas AccessGroup`](#schemas-accessgroup)
    - [Add shared component access group](#add-shared-component-access-group)
    - [Remove shared component access group](#remove-shared-component-access-group)
- [`LoginPortals`](#loginportals)
  - [Get a login portal](#get-a-login-portal)
  - [Update portal metadata](#update-portal-metadata)
  - [Delete a login portal](#delete-a-login-portal)
  - [Create a portal](#create-a-portal)
  - [List all portals](#list-all-portals)
- [`AccessGroups`](#accessgroups)
  - [Create an access group](#create-an-access-group)
  - [Get an access group](#get-an-access-group)
  - [Update an access group](#update-an-access-group)
  - [Delete an access group](#delete-an-access-group)
  - [`AccessGroups Domains`](#accessgroups-domains)
    - [Add an allowed email domain](#add-an-allowed-email-domain)
    - [Remove an allowed email domain](#remove-an-allowed-email-domain)
- [`Rules`](#rules)
  - [List all rules](#list-all-rules)
  - [Create a rule](#create-a-rule)
  - [Update rule metadata](#update-rule-metadata)
  - [Delete a rule](#delete-a-rule)
  - [Get a rule](#get-a-rule)
  - [Add rule access group](#add-rule-access-group)
  - [Remove rule access group](#remove-rule-access-group)
- [`Themes`](#themes)
  - [List all themes](#list-all-themes)
  - [Create a theme](#create-a-theme)
  - [Update theme metadata](#update-theme-metadata)
  - [Update theme document](#update-theme-document)
  - [Delete a theme](#delete-a-theme)
  - [Get a theme](#get-a-theme)
- [`Teams`](#teams)
  - [List teams](#list-teams)
  - [`Teams Members`](#teams-members)
    - [List team members](#list-team-members)
    - [Change a member role](#change-a-member-role)
    - [Remove a member](#remove-a-member)
  - [`Teams Invites`](#teams-invites)
    - [Invite a member](#invite-a-member)
    - [Resend an invite](#resend-an-invite)
    - [Cancel an invite](#cancel-an-invite)
- [`ScalarDocs`](#scalardocs)
  - [List all projects](#list-all-projects)
  - [Create a project](#create-a-project)
  - [Publish a project](#publish-a-project)
  - [List all docs projects](#list-all-docs-projects)
  - [Create a docs project](#create-a-docs-project)
  - [Get a docs project](#get-a-docs-project)
  - [Update a docs project](#update-a-docs-project)
  - [Delete a docs project](#delete-a-docs-project)
  - [Publish a docs project](#publish-a-docs-project)
  - [Read the site config](#read-the-site-config)
  - [Write the site config](#write-the-site-config)
  - [Get the site domains](#get-the-site-domains)
  - [Check domain DNS](#check-domain-dns)
- [`Namespaces`](#namespaces)
  - [List namespaces](#list-namespaces)
- [`Authentication`](#authentication)
  - [Exchange token](#exchange-token)
  - [Get current user](#get-current-user)
- [`Sdks`](#sdks)
  - [List all SDKs](#list-all-sdks)
  - [Create an SDK](#create-an-sdk)
  - [Get an SDK](#get-an-sdk)
  - [Update an SDK](#update-an-sdk)
  - [Delete an SDK](#delete-an-sdk)
  - [Build an SDK](#build-an-sdk)
  - [`Sdks Versions`](#sdks-versions)
    - [Create an SDK version](#create-an-sdk-version)
    - [Delete an SDK version](#delete-an-sdk-version)
  - [`Sdks Repositories`](#sdks-repositories)
    - [Link a repository](#link-a-repository)
    - [Unlink a repository](#unlink-a-repository)
    - [Update publishing settings](#update-publishing-settings)
- [`Mcp`](#mcp)
  - [`Mcp Servers`](#mcp-servers)
    - [List all MCP servers](#list-all-mcp-servers)
    - [Create an MCP server](#create-an-mcp-server)
    - [Get an MCP server](#get-an-mcp-server)
    - [Update an MCP server](#update-an-mcp-server)
    - [Delete an MCP server](#delete-an-mcp-server)
    - [`Mcp Servers Installations`](#mcp-servers-installations)
      - [List installations](#list-installations)
      - [Create an installation](#create-an-installation)
      - [Get an installation](#get-an-installation)
      - [Update an installation](#update-an-installation)
      - [Delete an installation](#delete-an-installation)
      - [Add an access group](#add-an-access-group)
      - [Remove an access group](#remove-an-access-group)
- [`OAuth`](#oauth)
  - [Start an OAuth authorization](#start-an-oauth-authorization)
  - [Exchange a code or refresh token](#exchange-a-code-or-refresh-token)
  - [Revoke a refresh token](#revoke-a-refresh-token)
  - [Authorization server metadata](#authorization-server-metadata)

## Setup

```python
import os

from scalar_sdk import Scalar

client = Scalar(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

## `Registry`

Registry

### List all API Documents

List all API documents across every namespace the caller can access.

| Direction | Type |
| --- | --- |
| Response | [`RegistryListAllAPIDocumentsResponse`](./src/scalar_sdk/types/registry_list_all_api_documents_response.py) |

```python
registry = client.registry.list_all_api_documents()
```

### List API Documents in a namespace

List API documents in a namespace.

| Direction | Type |
| --- | --- |
| Response | [`RegistryListAPIDocumentsResponse`](./src/scalar_sdk/types/registry_list_api_documents_response.py) |

```python
registry = client.registry.list_api_documents(
    namespace="acme",
)
```

### Create API Document

Create an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryCreateAPIDocumentParams`](./src/scalar_sdk/types/registry_create_api_document_params.py) |
| Response | [`RegistryCreateAPIDocumentResponse`](./src/scalar_sdk/types/registry_create_api_document_response.py) |

```python
registry = client.registry.create_api_document(
    namespace="acme",
    title="Acme API",
    version="1.2.0",
    slug="acme-api",
    document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
)
```

### Update API Document metadata

Update metadata for an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryUpdateAPIDocumentParams`](./src/scalar_sdk/types/registry_update_api_document_params.py) |
| Response | [`RegistryUpdateAPIDocumentResponse`](./src/scalar_sdk/types/registry_update_api_document_response.py) |

```python
registry = client.registry.update_api_document(
    namespace="acme",
    slug="acme-api",
)
```

### Delete API Document

Delete an API document and all versions.

| Direction | Type |
| --- | --- |
| Response | [`RegistryDeleteAPIDocumentResponse`](./src/scalar_sdk/types/registry_delete_api_document_response.py) |

```python
registry = client.registry.delete_api_document(
    namespace="acme",
    slug="acme-api",
)
```

### Get API Document

Get a specific API document version.

| Direction | Type |
| --- | --- |
| Response | [`RegistryRetrieveAPIDocumentVersionResponse`](./src/scalar_sdk/types/registry_retrieve_api_document_version_response.py) |

```python
registry = client.registry.retrieve_api_document_version(
    namespace="acme",
    slug="acme-api",
    semver="1.2.0",
)
```

### Update API Document version

Update the registry file content for an API document version.

| Direction | Type |
| --- | --- |
| Request | [`RegistryUpdateAPIDocumentVersionParams`](./src/scalar_sdk/types/registry_update_api_document_version_params.py) |
| Response | [`RegistryUpdateAPIDocumentVersionResponse`](./src/scalar_sdk/types/registry_update_api_document_version_response.py) |

```python
registry = client.registry.update_api_document_version(
    namespace="acme",
    slug="acme-api",
    semver="1.2.0",
    document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
)
```

### Delete API Document version

Delete a specific API document version.

| Direction | Type |
| --- | --- |
| Response | [`RegistryDeleteAPIDocumentVersionResponse`](./src/scalar_sdk/types/registry_delete_api_document_version_response.py) |

```python
registry = client.registry.delete_api_document_version(
    namespace="acme",
    slug="acme-api",
    semver="1.2.0",
)
```

### Get API Document version metadata

Get metadata (uid, content shas, version sha, tags) for a specific API document version.

| Direction | Type |
| --- | --- |
| Response | [`ManagedDocVersion`](./src/scalar_sdk/types/shared/managed_doc_version.py) |

```python
registry = client.registry.list_api_document_version_metadata(
    namespace="acme",
    slug="acme-api",
    semver="1.2.0",
)
```

### Create API Document version

Create a new API document version.

| Direction | Type |
| --- | --- |
| Request | [`RegistryCreateAPIDocumentVersionParams`](./src/scalar_sdk/types/registry_create_api_document_version_params.py) |
| Response | [`ManagedDocVersion`](./src/scalar_sdk/types/shared/managed_doc_version.py) |

```python
registry = client.registry.create_api_document_version(
    namespace="acme",
    slug="acme-api",
    version="1.2.0",
    document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
)
```

### Add access group

Add an access group to an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryCreateAPIDocumentAccessGroupParams`](./src/scalar_sdk/types/registry_create_api_document_access_group_params.py) |
| Response | [`RegistryCreateAPIDocumentAccessGroupResponse`](./src/scalar_sdk/types/registry_create_api_document_access_group_response.py) |

```python
registry = client.registry.create_api_document_access_group(
    namespace="acme",
    slug="acme-api",
    access_group_slug="acme-api",
)
```

### Remove access group

Remove an access group from an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryDeleteAPIDocumentAccessGroupParams`](./src/scalar_sdk/types/registry_delete_api_document_access_group_params.py) |
| Response | [`RegistryDeleteAPIDocumentAccessGroupResponse`](./src/scalar_sdk/types/registry_delete_api_document_access_group_response.py) |

```python
registry = client.registry.delete_api_document_access_group(
    namespace="acme",
    slug="acme-api",
    access_group_slug="acme-api",
)
```

## `Schemas`

Schemas

### List all shared components

List schemas in a namespace.

| Direction | Type |
| --- | --- |
| Response | [`SchemaListResponse`](./src/scalar_sdk/types/schema_list_response.py) |

```python
schema = client.schemas.list(
    namespace="acme",
)
```

### Create a shared component

Create a schema in a namespace.

| Direction | Type |
| --- | --- |
| Request | [`SchemaCreateParams`](./src/scalar_sdk/types/schema_create_params.py) |
| Response | [`UID`](./src/scalar_sdk/types/shared/uid.py) |

```python
schema = client.schemas.create(
    namespace="acme",
    title="Customer",
    version="1.2.0",
    slug="customer",
    document='{"type":"object","properties":{"name":{"type":"string","examples":["Acme"]}}}',
)
```

### Update shared component metadata

Update schema metadata.

| Direction | Type |
| --- | --- |
| Request | [`SchemaUpdateParams`](./src/scalar_sdk/types/schema_update_params.py) |
| Response | [`SchemaUpdateResponse`](./src/scalar_sdk/types/schema_update_response.py) |

```python
schema = client.schemas.update(
    namespace="acme",
    slug="customer",
)
```

### Delete a shared component

Delete a schema and all related versions.

| Direction | Type |
| --- | --- |
| Response | [`SchemaDeleteResponse`](./src/scalar_sdk/types/schema_delete_response.py) |

```python
schema = client.schemas.delete(
    namespace="acme",
    slug="customer",
)
```

### `Schemas Version`

Schemas

#### Get a shared component document

Get a specific schema version document.

| Direction | Type |
| --- | --- |
| Response | [`VersionRetrieveResponse`](./src/scalar_sdk/types/schemas/version_retrieve_response.py) |

```python
version = client.schemas.version.retrieve(
    namespace="acme",
    slug="customer",
    semver="1.2.0",
)
```

#### Delete a shared component version

Delete a schema version.

| Direction | Type |
| --- | --- |
| Response | [`VersionDeleteResponse`](./src/scalar_sdk/types/schemas/version_delete_response.py) |

```python
version = client.schemas.version.delete(
    namespace="acme",
    slug="customer",
    semver="1.2.0",
)
```

#### Create a shared component version

Create a schema version.

| Direction | Type |
| --- | --- |
| Request | [`VersionCreateParams`](./src/scalar_sdk/types/schemas/version_create_params.py) |
| Response | [`VersionCreateResponse`](./src/scalar_sdk/types/schemas/version_create_response.py) |

```python
version = client.schemas.version.create(
    namespace="acme",
    slug="customer",
    version="1.2.0",
    document='{"type":"object","properties":{"name":{"type":"string","examples":["Acme"]}}}',
)
```

### `Schemas AccessGroup`

Schemas

#### Add shared component access group

Add an access group to a schema.

| Direction | Type |
| --- | --- |
| Request | [`AccessGroupCreateParams`](./src/scalar_sdk/types/schemas/access_group_create_params.py) |
| Response | [`AccessGroupCreateResponse`](./src/scalar_sdk/types/schemas/access_group_create_response.py) |

```python
access_group = client.schemas.access_group.create(
    namespace="acme",
    slug="customer",
    access_group_slug="acme-api",
)
```

#### Remove shared component access group

Remove an access group from a schema.

| Direction | Type |
| --- | --- |
| Request | [`AccessGroupDeleteParams`](./src/scalar_sdk/types/schemas/access_group_delete_params.py) |
| Response | [`AccessGroupDeleteResponse`](./src/scalar_sdk/types/schemas/access_group_delete_response.py) |

```python
access_group = client.schemas.access_group.delete(
    namespace="acme",
    slug="customer",
    access_group_slug="acme-api",
)
```

## `LoginPortals`

Login Portals

### Get a login portal

Get a login portal by slug.

| Direction | Type |
| --- | --- |
| Response | [`LoginPortalRetrieveResponse`](./src/scalar_sdk/types/login_portal_retrieve_response.py) |

```python
login_portal = client.login_portals.retrieve(
    slug="acme-login",
)
```

### Update portal metadata

Update metadata for a login portal.

| Direction | Type |
| --- | --- |
| Request | [`LoginPortalUpdateParams`](./src/scalar_sdk/types/login_portal_update_params.py) |
| Response | [`LoginPortalUpdateResponse`](./src/scalar_sdk/types/login_portal_update_response.py) |

```python
login_portal = client.login_portals.update(
    slug="acme-login",
)
```

### Delete a login portal

Delete a login portal.

| Direction | Type |
| --- | --- |
| Response | [`LoginPortalDeleteResponse`](./src/scalar_sdk/types/login_portal_delete_response.py) |

```python
login_portal = client.login_portals.delete(
    slug="acme-login",
)
```

### Create a portal

Create a login portal for the current team.

| Direction | Type |
| --- | --- |
| Request | [`LoginPortalCreateParams`](./src/scalar_sdk/types/login_portal_create_params.py) |
| Response | [`UID`](./src/scalar_sdk/types/shared/uid.py) |

```python
login_portal = client.login_portals.create(
    title="Acme Private Documentation",
    slug="acme-login",
    email={
        "logo": "",
        "logo_size": "100",
        "button_text": "Login",
        "message": "Click to access private documentation hosted by scalar.com",
        "title": "Private Docs",
        "main_color": "#2a2f45",
        "main_background": "#f6f6f6",
        "card_color": "#2a2f45",
        "card_background": "#fff",
        "button_color": "#fff",
        "button_background": "#0f0f0f",
    },
    page={
        "title": "Scalar Private Docs",
        "description": "Login to access your documentation",
        "head": "",
        "script": "",
        "theme": "",
        "company_name": "",
        "logo": "",
        "logo_url": "",
        "favicon": "",
        "terms_link": "",
        "privacy_link": "",
        "form_title": "Scalar Private Docs",
        "form_description": "Login to access your documentation",
        "form_image": "",
    },
)
```

### List all portals

List all login portals for the current team.

| Direction | Type |
| --- | --- |
| Response | [`LoginPortalListResponse`](./src/scalar_sdk/types/login_portal_list_response.py) |

```python
login_portal = client.login_portals.list()
```

## `AccessGroups`

Access Groups

### Create an access group

Create a group for the current team. Requires docs edit permission and the access groups billing feature. Domains are exact email domains, without wildcards or implicit subdomain matching.

| Direction | Type |
| --- | --- |
| Request | [`AccessGroupCreateParams`](./src/scalar_sdk/types/access_group_create_params.py) |
| Response | [`AccessGroupCreateResponse`](./src/scalar_sdk/types/access_group_create_response.py) |

```python
access_group = client.access_groups.create()
```

### Get an access group

Get a group and its email and domain allowlists by slug.

| Direction | Type |
| --- | --- |
| Response | [`AccessGroupRetrieveResponse`](./src/scalar_sdk/types/access_group_retrieve_response.py) |

```python
access_group = client.access_groups.retrieve(
    slug="acme-api",
)
```

### Update an access group

Update group metadata. Requires docs edit permission. After changing the slug, use the new slug in subsequent requests.

| Direction | Type |
| --- | --- |
| Request | [`AccessGroupUpdateParams`](./src/scalar_sdk/types/access_group_update_params.py) |
| Response | [`AccessGroupUpdateResponse`](./src/scalar_sdk/types/access_group_update_response.py) |

```python
access_group = client.access_groups.update(
    path_slug="acme-api",
)
```

### Delete an access group

Delete a group and remove its project assignments. Requires docs edit permission.

| Direction | Type |
| --- | --- |
| Response | [`AccessGroupDeleteResponse`](./src/scalar_sdk/types/access_group_delete_response.py) |

```python
access_group = client.access_groups.delete(
    slug="acme-api",
)
```

### `AccessGroups Domains`

Access Groups

#### Add an allowed email domain

Allow an exact email domain in a group. Requires docs edit permission. A group supports up to 1000 domains.

| Direction | Type |
| --- | --- |
| Request | [`DomainCreateParams`](./src/scalar_sdk/types/access_groups/domain_create_params.py) |
| Response | [`DomainCreateResponse`](./src/scalar_sdk/types/access_groups/domain_create_response.py) |

```python
domain = client.access_groups.domains.create(
    slug="acme-api",
    domain="example.com",
)
```

#### Remove an allowed email domain

Remove an exact email domain from a group. Requires docs edit permission. Other allowed domains and emails are preserved.

| Direction | Type |
| --- | --- |
| Request | [`DomainDeleteParams`](./src/scalar_sdk/types/access_groups/domain_delete_params.py) |
| Response | [`DomainDeleteResponse`](./src/scalar_sdk/types/access_groups/domain_delete_response.py) |

```python
domain = client.access_groups.domains.delete(
    slug="acme-api",
    domain="example.com",
)
```

## `Rules`

Rules

### List all rules

List all rulesets in a namespace.

| Direction | Type |
| --- | --- |
| Response | [`RuleListRulesetsResponse`](./src/scalar_sdk/types/rule_list_rulesets_response.py) |

```python
rule = client.rules.list_rulesets(
    namespace="acme",
)
```

### Create a rule

Create a rule in a namespace.

| Direction | Type |
| --- | --- |
| Request | [`RuleCreateRulesetParams`](./src/scalar_sdk/types/rule_create_ruleset_params.py) |
| Response | [`UID`](./src/scalar_sdk/types/shared/uid.py) |

```python
rule = client.rules.create_ruleset(
    namespace="acme",
    title="Acme API Rules",
    slug="acme-rules",
    document='extends: ["spectral:oas"]\nrules:\n  info-contact: warn\n',
)
```

### Update rule metadata

Update rule metadata by slug.

| Direction | Type |
| --- | --- |
| Request | [`RuleUpdateRulesetParams`](./src/scalar_sdk/types/rule_update_ruleset_params.py) |
| Response | [`RuleUpdateRulesetResponse`](./src/scalar_sdk/types/rule_update_ruleset_response.py) |

```python
rule = client.rules.update_ruleset(
    path_namespace="acme",
    path_slug="acme-rules",
)
```

### Delete a rule

Delete a rule by slug.

| Direction | Type |
| --- | --- |
| Response | [`RuleDeleteRulesetResponse`](./src/scalar_sdk/types/rule_delete_ruleset_response.py) |

```python
rule = client.rules.delete_ruleset(
    namespace="acme",
    slug="acme-rules",
)
```

### Get a rule

Get a rule document by slug.

| Direction | Type |
| --- | --- |
| Response | [`RuleRetrieveRulesetDocumentResponse`](./src/scalar_sdk/types/rule_retrieve_ruleset_document_response.py) |

```python
rule = client.rules.retrieve_ruleset_document(
    namespace="acme",
    slug="acme-rules",
)
```

### Add rule access group

Grant an access group to a rule.

| Direction | Type |
| --- | --- |
| Request | [`RuleCreateRulesetAccessGroupParams`](./src/scalar_sdk/types/rule_create_ruleset_access_group_params.py) |
| Response | [`RuleCreateRulesetAccessGroupResponse`](./src/scalar_sdk/types/rule_create_ruleset_access_group_response.py) |

```python
rule = client.rules.create_ruleset_access_group(
    namespace="acme",
    slug="acme-rules",
    access_group_slug="acme-api",
)
```

### Remove rule access group

Remove an access group from a rule.

| Direction | Type |
| --- | --- |
| Request | [`RuleDeleteRulesetAccessGroupParams`](./src/scalar_sdk/types/rule_delete_ruleset_access_group_params.py) |
| Response | [`RuleDeleteRulesetAccessGroupResponse`](./src/scalar_sdk/types/rule_delete_ruleset_access_group_response.py) |

```python
rule = client.rules.delete_ruleset_access_group(
    namespace="acme",
    slug="acme-rules",
    access_group_slug="acme-api",
)
```

## `Themes`

Themes

### List all themes

List all team themes.

| Direction | Type |
| --- | --- |
| Response | [`ThemeListResponse`](./src/scalar_sdk/types/theme_list_response.py) |

```python
theme = client.themes.list()
```

### Create a theme

Create a team theme.

| Direction | Type |
| --- | --- |
| Request | [`ThemeCreateParams`](./src/scalar_sdk/types/theme_create_params.py) |
| Response | [`UID`](./src/scalar_sdk/types/shared/uid.py) |

```python
theme = client.themes.create(
    name="Acme Theme",
    slug="acme-theme",
    document=":root { --scalar-color-1: #1f2937; }",
)
```

### Update theme metadata

Update theme metadata.

| Direction | Type |
| --- | --- |
| Request | [`ThemeUpdateParams`](./src/scalar_sdk/types/theme_update_params.py) |
| Response | [`ThemeUpdateResponse`](./src/scalar_sdk/types/theme_update_response.py) |

```python
theme = client.themes.update(
    slug="acme-theme",
)
```

### Update theme document

Replace the theme document.

| Direction | Type |
| --- | --- |
| Request | [`ThemeReplaceDocumentParams`](./src/scalar_sdk/types/theme_replace_document_params.py) |
| Response | [`ThemeReplaceDocumentResponse`](./src/scalar_sdk/types/theme_replace_document_response.py) |

```python
theme = client.themes.replace_document(
    slug="acme-theme",
    document=":root { --scalar-color-1: #1f2937; }",
)
```

### Delete a theme

Delete a theme by slug.

| Direction | Type |
| --- | --- |
| Response | [`ThemeDeleteResponse`](./src/scalar_sdk/types/theme_delete_response.py) |

```python
theme = client.themes.delete(
    slug="acme-theme",
)
```

### Get a theme

Get the theme document by slug.

| Direction | Type |
| --- | --- |
| Response | [`ThemeRetrieveResponse`](./src/scalar_sdk/types/theme_retrieve_response.py) |

```python
theme = client.themes.retrieve(
    slug="acme-theme",
)
```

## `Teams`

Teams

### List teams

List all available teams

| Direction | Type |
| --- | --- |
| Response | [`TeamListResponse`](./src/scalar_sdk/types/team_list_response.py) |

```python
team = client.teams.list()
```

### `Teams Members`

Teams

#### List team members

List the members of the current team, along with the invites still outstanding.

| Direction | Type |
| --- | --- |
| Response | [`MemberListResponse`](./src/scalar_sdk/types/teams/member_list_response.py) |

```python
member = client.teams.members.list()
```

#### Change a member role

Change what a member of the current team is allowed to do.

| Direction | Type |
| --- | --- |
| Request | [`MemberUpdateParams`](./src/scalar_sdk/types/teams/member_update_params.py) |
| Response | [`MemberUpdateResponse`](./src/scalar_sdk/types/teams/member_update_response.py) |

```python
member = client.teams.members.update(
    uid="UakgbKJ5m9gl0JDMbcJqL",
    role="owner",
)
```

#### Remove a member

Remove someone from the current team.

| Direction | Type |
| --- | --- |
| Response | [`MemberDeleteResponse`](./src/scalar_sdk/types/teams/member_delete_response.py) |

```python
member = client.teams.members.delete(
    uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

### `Teams Invites`

Teams

#### Invite a member

Invite someone to the current team by email.

| Direction | Type |
| --- | --- |
| Request | [`InviteMemberParams`](./src/scalar_sdk/types/teams/invite_member_params.py) |
| Response | [`InviteMemberResponse`](./src/scalar_sdk/types/teams/invite_member_response.py) |

```python
invite = client.teams.invites.member(
    email="alex@example.com",
    role="owner",
)
```

#### Resend an invite

Send the invite email again.

| Direction | Type |
| --- | --- |
| Response | [`InviteResendResponse`](./src/scalar_sdk/types/teams/invite_resend_response.py) |

```python
invite = client.teams.invites.resend(
    uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

#### Cancel an invite

Withdraw an invite that has not been accepted.

| Direction | Type |
| --- | --- |
| Response | [`InviteCancelResponse`](./src/scalar_sdk/types/teams/invite_cancel_response.py) |

```python
invite = client.teams.invites.cancel(
    uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

## `ScalarDocs`

Scalar Docs

### List all projects

List all guide projects.

| Direction | Type |
| --- | --- |
| Response | [`ScalarDocListGuidesResponse`](./src/scalar_sdk/types/scalar_doc_list_guides_response.py) |

```python
scalar_doc = client.scalar_docs.list_guides()
```

### Create a project

Create a guide project.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocCreateGuideParams`](./src/scalar_sdk/types/scalar_doc_create_guide_params.py) |
| Response | [`ScalarDocCreateGuideResponse`](./src/scalar_sdk/types/scalar_doc_create_guide_response.py) |

```python
scalar_doc = client.scalar_docs.create_guide(
    name="Acme Documentation",
    is_private=False,
    allowed_users=[],
    allowed_domains=[],
)
```

### Publish a project

Start a new publish process.

| Direction | Type |
| --- | --- |
| Response | [`ScalarDocPublishGuideResponse`](./src/scalar_sdk/types/scalar_doc_publish_guide_response.py) |

```python
scalar_doc = client.scalar_docs.publish_guide(
    slug="acme-docs",
)
```

### List all docs projects

List every docs project on the team.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocListProjectsParams`](./src/scalar_sdk/types/scalar_doc_list_projects_params.py) |
| Response | [`ScalarDocListProjectsResponse`](./src/scalar_sdk/types/scalar_doc_list_projects_response.py) |

```python
scalar_doc = client.scalar_docs.list_projects()
```

### Create a docs project

Create a docs project. Omit `provider` to have Scalar host the repository.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocCreateProjectParams`](./src/scalar_sdk/types/scalar_doc_create_project_params.py) |
| Response | [`DocsProject`](./src/scalar_sdk/types/docs_project.py) |

```python
scalar_doc = client.scalar_docs.create_project(
    name="Acme Documentation",
    provider="forgejo",
)
```

### Get a docs project

Get a single docs project by its slug.

| Direction | Type |
| --- | --- |
| Response | [`DocsProject`](./src/scalar_sdk/types/docs_project.py) |

```python
scalar_doc = client.scalar_docs.retrieve_project(
    slug="acme-docs",
)
```

### Update a docs project

Update project settings. Set `isPrivate` with `accessGroups` to put the site behind a login.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocUpdateProjectParams`](./src/scalar_sdk/types/scalar_doc_update_project_params.py) |
| Response | [`ScalarDocUpdateProjectResponse`](./src/scalar_sdk/types/scalar_doc_update_project_response.py) |

```python
scalar_doc = client.scalar_docs.update_project(
    slug="acme-docs",
)
```

### Delete a docs project

Delete a docs project, its deploys, its publish records and its cached builds.

| Direction | Type |
| --- | --- |
| Response | [`ScalarDocDeleteProjectResponse`](./src/scalar_sdk/types/scalar_doc_delete_project_response.py) |

```python
scalar_doc = client.scalar_docs.delete_project(
    slug="acme-docs",
)
```

### Publish a docs project

Start a build and deploy. The returned `publishUid` identifies the publish record.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocPublishProjectParams`](./src/scalar_sdk/types/scalar_doc_publish_project_params.py) |
| Response | [`ScalarDocPublishProjectResponse`](./src/scalar_sdk/types/scalar_doc_publish_project_response.py) |

```python
scalar_doc = client.scalar_docs.publish_project(
    slug="acme-docs",
)
```

### Read the site config

Read `scalar.config.json` straight from the project repository, without cloning it. `baseToken` is the compare-and-swap handle for a later write.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocListProjectConfigParams`](./src/scalar_sdk/types/scalar_doc_list_project_config_params.py) |
| Response | [`ScalarDocListProjectConfigResponse`](./src/scalar_sdk/types/scalar_doc_list_project_config_response.py) |

```python
scalar_doc = client.scalar_docs.list_project_config(
    slug="acme-docs",
)
```

### Write the site config

Commit `scalar.config.json` straight to the project repository. Pass the `baseToken` from the read this edit was based on; a conflict means the file moved underneath it.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocUpdateProjectConfigParams`](./src/scalar_sdk/types/scalar_doc_update_project_config_params.py) |
| Response | [`ScalarDocUpdateProjectConfigResponse`](./src/scalar_sdk/types/scalar_doc_update_project_config_response.py) |

```python
scalar_doc = client.scalar_docs.update_project_config(
    slug="acme-docs",
    content='{"name":"Acme Documentation"}',
)
```

### Get the site domains

The domains the project serves on — the Scalar-hosted one and the custom one, when set.

| Direction | Type |
| --- | --- |
| Response | [`ScalarDocListProjectDomainResponse`](./src/scalar_sdk/types/scalar_doc_list_project_domain_response.py) |

```python
scalar_doc = client.scalar_docs.list_project_domain(
    slug="acme-docs",
)
```

### Check domain DNS

Whether the project custom domain points at Scalar yet. `expected` is the CNAME record to create; `found` is what resolves today. A project with no custom domain reports `verified` with no expected record, because Scalar serves its own subdomain directly.

| Direction | Type |
| --- | --- |
| Response | [`ScalarDocListProjectDomainStatusResponse`](./src/scalar_sdk/types/scalar_doc_list_project_domain_status_response.py) |

```python
scalar_doc = client.scalar_docs.list_project_domain_status(
    slug="acme-docs",
)
```

## `Namespaces`

Namespaces

### List namespaces

Get all namespaces for the current team

| Direction | Type |
| --- | --- |
| Response | [`NamespaceListResponse`](./src/scalar_sdk/types/namespace_list_response.py) |

```python
namespace = client.namespaces.list()
```

## `Authentication`

Authentication

### Exchange token

Exchange an API key for an access token.

| Direction | Type |
| --- | --- |
| Request | [`AuthenticationExchangePersonalTokenParams`](./src/scalar_sdk/types/authentication_exchange_personal_token_params.py) |
| Response | [`AuthenticationExchangePersonalTokenResponse`](./src/scalar_sdk/types/authentication_exchange_personal_token_response.py) |

```python
authentication = client.authentication.exchange_personal_token(
    personal_token="scalar_example_personal_token",
)
```

### Get current user

Get the authenticated user, including their available teams and theme.

| Direction | Type |
| --- | --- |
| Response | [`User`](./src/scalar_sdk/types/teams/user.py) |

```python
authentication = client.authentication.list_current_user()
```

## `Sdks`

SDKs

### List all SDKs

List every SDK on the team.

| Direction | Type |
| --- | --- |
| Request | [`SdkListParams`](./src/scalar_sdk/types/sdk_list_params.py) |
| Response | [`SdkListResponse`](./src/scalar_sdk/types/sdk_list_response.py) |

```python
sdk = client.sdks.list()
```

### Create an SDK

Create an SDK from an API document, targeting one or more languages.

| Direction | Type |
| --- | --- |
| Request | [`SdkCreateParams`](./src/scalar_sdk/types/sdk_create_params.py) |
| Response | [`UID`](./src/scalar_sdk/types/shared/uid.py) |

```python
sdk = client.sdks.create(
    api_uid="UakgbKJ5m9gl0JDMbcJqL",
    languages=["typescript"],
)
```

### Get an SDK

Get a single SDK by its uid.

| Direction | Type |
| --- | --- |
| Response | [`Sdk`](./src/scalar_sdk/types/sdk.py) |

```python
sdk = client.sdks.retrieve(
    uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

### Update an SDK

Update SDK metadata, its linked API, or its config.

| Direction | Type |
| --- | --- |
| Request | [`SdkUpdateParams`](./src/scalar_sdk/types/sdk_update_params.py) |
| Response | [`SdkUpdateResponse`](./src/scalar_sdk/types/sdk_update_response.py) |

```python
sdk = client.sdks.update(
    uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

### Delete an SDK

Delete an SDK and every version it holds.

| Direction | Type |
| --- | --- |
| Response | [`SdkDeleteResponse`](./src/scalar_sdk/types/sdk_delete_response.py) |

```python
sdk = client.sdks.delete(
    uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

### Build an SDK

Start a build. Omit `version` to build the current work — the open draft, else the latest version — and the resolved version comes back in the response.

| Direction | Type |
| --- | --- |
| Request | [`SdkBuildParams`](./src/scalar_sdk/types/sdk_build_params.py) |
| Response | [`SdkBuildResponse`](./src/scalar_sdk/types/sdk_build_response.py) |

```python
sdk = client.sdks.build(
    uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

### `Sdks Versions`

SDKs

#### Create an SDK version

Create a new SDK version against a specific API version.

| Direction | Type |
| --- | --- |
| Request | [`VersionCreateParams`](./src/scalar_sdk/types/sdks/version_create_params.py) |
| Response | [`VersionCreateResponse`](./src/scalar_sdk/types/sdks/version_create_response.py) |

```python
version = client.sdks.versions.create(
    uid="UakgbKJ5m9gl0JDMbcJqL",
    version="1.2.0",
    api_version="1.2.0",
)
```

#### Delete an SDK version

Permanently delete one version of an SDK.

| Direction | Type |
| --- | --- |
| Response | [`VersionDeleteResponse`](./src/scalar_sdk/types/sdks/version_delete_response.py) |

```python
version = client.sdks.versions.delete(
    uid="UakgbKJ5m9gl0JDMbcJqL",
    version="1.2.0",
)
```

### `Sdks Repositories`

SDKs

#### Link a repository

Link one language target to a GitHub repository, so builds sync there.

| Direction | Type |
| --- | --- |
| Request | [`RepositoryLinkParams`](./src/scalar_sdk/types/sdks/repository_link_params.py) |
| Response | [`RepositoryLinkResponse`](./src/scalar_sdk/types/sdks/repository_link_response.py) |

```python
repository = client.sdks.repositories.link(
    uid="UakgbKJ5m9gl0JDMbcJqL",
    language="typescript",
    repository_id=123456789,
    base_branch="main",
)
```

#### Unlink a repository

Unlink one language target from its repository.

| Direction | Type |
| --- | --- |
| Response | [`RepositoryUnlinkResponse`](./src/scalar_sdk/types/sdks/repository_unlink_response.py) |

```python
repository = client.sdks.repositories.unlink(
    uid="UakgbKJ5m9gl0JDMbcJqL",
    language="typescript",
)
```

#### Update publishing settings

Toggle publish-on-merge and the release settings for a linked target.

| Direction | Type |
| --- | --- |
| Request | [`RepositoryUpdatePublishingParams`](./src/scalar_sdk/types/sdks/repository_update_publishing_params.py) |
| Response | [`RepositoryUpdatePublishingResponse`](./src/scalar_sdk/types/sdks/repository_update_publishing_response.py) |

```python
repository = client.sdks.repositories.update_publishing(
    uid="UakgbKJ5m9gl0JDMbcJqL",
    language="typescript",
    publish_on_merge=True,
)
```

## `Mcp`

### `Mcp Servers`

MCP

#### List all MCP servers

List every MCP server on the team.

| Direction | Type |
| --- | --- |
| Response | [`ServerListResponse`](./src/scalar_sdk/types/mcp/server_list_response.py) |

```python
server = client.mcp.servers.list()
```

#### Create an MCP server

Create an MCP server over one or more API document versions. The response carries the server and its first installation.

| Direction | Type |
| --- | --- |
| Request | [`ServerCreateParams`](./src/scalar_sdk/types/mcp/server_create_params.py) |
| Response | [`ServerCreateResponse`](./src/scalar_sdk/types/mcp/server_create_response.py) |

```python
server = client.mcp.servers.create(
    name="Acme MCP",
)
```

#### Get an MCP server

Get a single MCP server by its id.

| Direction | Type |
| --- | --- |
| Response | [`McpServer`](./src/scalar_sdk/types/mcp/mcp_server.py) |

```python
server = client.mcp.servers.retrieve(
    id="42",
)
```

#### Update an MCP server

Update MCP server metadata and which tools it exposes.

| Direction | Type |
| --- | --- |
| Request | [`ServerUpdateParams`](./src/scalar_sdk/types/mcp/server_update_params.py) |
| Response | [`McpServer`](./src/scalar_sdk/types/mcp/mcp_server.py) |

```python
server = client.mcp.servers.update(
    id="42",
)
```

#### Delete an MCP server

Delete an MCP server and every installation it serves.

| Direction | Type |
| --- | --- |
| Response | [`ServerDeleteResponse`](./src/scalar_sdk/types/mcp/server_delete_response.py) |

```python
server = client.mcp.servers.delete(
    id="42",
)
```

#### `Mcp Servers Installations`

MCP

##### List installations

List the installations of an MCP server. An installation is what an MCP client connects to.

| Direction | Type |
| --- | --- |
| Response | [`InstallationListResponse`](./src/scalar_sdk/types/mcp/servers/installation_list_response.py) |

```python
installation = client.mcp.servers.installations.list(
    id="42",
)
```

##### Create an installation

Create an installation of an MCP server. `documentAuth` holds the credentials the server presents to the upstream API and is never returned.

| Direction | Type |
| --- | --- |
| Request | [`InstallationCreateParams`](./src/scalar_sdk/types/mcp/servers/installation_create_params.py) |
| Response | [`McpInstallation`](./src/scalar_sdk/types/mcp/mcp_installation.py) |

```python
installation = client.mcp.servers.installations.create(
    id="42",
    name="Acme MCP",
    document_auth={},
)
```

##### Get an installation

Get a single installation of an MCP server.

| Direction | Type |
| --- | --- |
| Response | [`McpInstallation`](./src/scalar_sdk/types/mcp/mcp_installation.py) |

```python
installation = client.mcp.servers.installations.retrieve(
    id="42",
    installation_id="84",
)
```

##### Update an installation

Update an installation. Set `isPrivate` and add access groups to put it behind a login.

| Direction | Type |
| --- | --- |
| Request | [`InstallationUpdateParams`](./src/scalar_sdk/types/mcp/servers/installation_update_params.py) |
| Response | [`McpInstallation`](./src/scalar_sdk/types/mcp/mcp_installation.py) |

```python
installation = client.mcp.servers.installations.update(
    id="42",
    installation_id="84",
)
```

##### Delete an installation

Delete an installation of an MCP server.

| Direction | Type |
| --- | --- |
| Response | [`InstallationDeleteResponse`](./src/scalar_sdk/types/mcp/servers/installation_delete_response.py) |

```python
installation = client.mcp.servers.installations.delete(
    id="42",
    installation_id="84",
)
```

##### Add an access group

Let an access group reach a private installation.

| Direction | Type |
| --- | --- |
| Request | [`InstallationCreateAccessGroupParams`](./src/scalar_sdk/types/mcp/servers/installation_create_access_group_params.py) |
| Response | [`InstallationCreateAccessGroupResponse`](./src/scalar_sdk/types/mcp/servers/installation_create_access_group_response.py) |

```python
installation = client.mcp.servers.installations.create_access_group(
    id="42",
    installation_id="84",
    access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

##### Remove an access group

Stop an access group reaching a private installation.

| Direction | Type |
| --- | --- |
| Request | [`InstallationDeleteAccessGroupParams`](./src/scalar_sdk/types/mcp/servers/installation_delete_access_group_params.py) |
| Response | [`InstallationDeleteAccessGroupResponse`](./src/scalar_sdk/types/mcp/servers/installation_delete_access_group_response.py) |

```python
installation = client.mcp.servers.installations.delete_access_group(
    id="42",
    installation_id="84",
    access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
)
```

## `OAuth`

OAuth

### Start an OAuth authorization

Authorization endpoint (RFC 6749 §4.1.1 with PKCE, RFC 7636). Validates the request and sends the user to the Scalar dashboard to approve it; the user returns to `redirect_uri` with a `code` to exchange at the token endpoint. Only `response_type=code` with `code_challenge_method=S256` is supported.

| Direction | Type |
| --- | --- |
| Response | [`OAuthOauthAuthorizeResponse`](./src/scalar_sdk/types/o_auth_oauth_authorize_response.py) |

```python
o_auth = client.o_auth.oauth_authorize()
```

### Exchange a code or refresh token

Token endpoint (RFC 6749 §4.1.3 and §6). Accepts `application/x-www-form-urlencoded`. Confidential clients authenticate with HTTP Basic or `client_secret` in the body; public clients send `client_id` alone. The `authorization_code` grant needs `code`, `redirect_uri` and `code_verifier`; the `refresh_token` grant needs `refresh_token` and may narrow `scope`.

| Direction | Type |
| --- | --- |
| Request | [`OAuthOauthTokenParams`](./src/scalar_sdk/types/o_auth_oauth_token_params.py) |
| Response | [`OAuthOauthTokenResponse`](./src/scalar_sdk/types/o_auth_oauth_token_response.py) |

```python
o_auth = client.o_auth.oauth_token(
    grant_type="",
)
```

### Revoke a refresh token

Revocation endpoint (RFC 7009). Revokes the refresh token and every token issued alongside it. The client authenticates as it does at the token endpoint. Responds 200 whether or not the token was live, as the RFC requires.

| Direction | Type |
| --- | --- |
| Request | [`OAuthOauthRevokeParams`](./src/scalar_sdk/types/o_auth_oauth_revoke_params.py) |
| Response | [`OAuthOauthRevokeResponse`](./src/scalar_sdk/types/o_auth_oauth_revoke_response.py) |

```python
o_auth = client.o_auth.oauth_revoke(
    token="",
)
```

### Authorization server metadata

Discovery document for OAuth clients (RFC 8414): where the endpoints are and what they support.

| Direction | Type |
| --- | --- |
| Response | [`OauthAuthorizationServerMetadata`](./src/scalar_sdk/types/oauth_authorization_server_metadata.py) |

```python
o_auth = client.o_auth.oauth_authorization_server_metadata()
```
