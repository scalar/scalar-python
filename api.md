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
- [`ScalarDocs`](#scalardocs)
  - [List all projects](#list-all-projects)
  - [Create a project](#create-a-project)
  - [Publish a project](#publish-a-project)
- [`Namespaces`](#namespaces)
  - [List namespaces](#list-namespaces)
- [`Authentication`](#authentication)
  - [Exchange token](#exchange-token)
  - [Get current user](#get-current-user)

## Setup

```python
import os

from scalar_api import ScalarApi

client = ScalarApi(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

## `Registry`

### List all API Documents

List all API documents across every namespace the caller can access.

| Direction | Type |
| --- | --- |
| Response | [`RegistryListAllApiDocumentsResponse`](./src/types/registry_list_all_api_documents_response.py) |

```python
registry = client.registry.list_all_api_documents()
```

### List API Documents in a namespace

List API documents in a namespace.

| Direction | Type |
| --- | --- |
| Response | [`RegistryListApiDocumentsResponse`](./src/types/registry_list_api_documents_response.py) |

```python
registry = client.registry.list_api_documents(
    namespace="namespace",
)
```

### Create API Document

Create an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryCreateApiDocumentParams`](./src/types/registry_create_api_document_params.py) |
| Response | [`RegistryCreateApiDocumentResponse`](./src/types/registry_create_api_document_response.py) |

```python
registry = client.registry.create_api_document(
    namespace="namespace",
    title="",
    version="",
    slug="",
    document="",
    idempotency_key="",
)
```

### Update API Document metadata

Update metadata for an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryUpdateApiDocumentParams`](./src/types/registry_update_api_document_params.py) |
| Response | [`RegistryUpdateApiDocumentResponse`](./src/types/registry_update_api_document_response.py) |

```python
registry = client.registry.update_api_document(
    namespace="namespace",
    slug="slug",
    idempotency_key="",
)
```

### Delete API Document

Delete an API document and all versions.

| Direction | Type |
| --- | --- |
| Response | [`RegistryDeleteApiDocumentResponse`](./src/types/registry_delete_api_document_response.py) |

```python
registry = client.registry.delete_api_document(
    namespace="namespace",
    slug="slug",
    idempotency_key="",
)
```

### Get API Document

Get a specific API document version.

| Direction | Type |
| --- | --- |
| Response | [`RegistryRetrieveApiDocumentVersionResponse`](./src/types/registry_retrieve_api_document_version_response.py) |

```python
registry = client.registry.retrieve_api_document_version(
    namespace="namespace",
    slug="slug",
    semver="semver",
)
```

### Update API Document version

Update the registry file content for an API document version.

| Direction | Type |
| --- | --- |
| Request | [`RegistryUpdateApiDocumentVersionParams`](./src/types/registry_update_api_document_version_params.py) |
| Response | [`RegistryUpdateApiDocumentVersionResponse`](./src/types/registry_update_api_document_version_response.py) |

```python
registry = client.registry.update_api_document_version(
    namespace="namespace",
    slug="slug",
    semver="semver",
    document="",
    idempotency_key="",
)
```

### Delete API Document version

Delete a specific API document version.

| Direction | Type |
| --- | --- |
| Response | [`RegistryDeleteApiDocumentVersionResponse`](./src/types/registry_delete_api_document_version_response.py) |

```python
registry = client.registry.delete_api_document_version(
    namespace="namespace",
    slug="slug",
    semver="semver",
    idempotency_key="",
)
```

### Get API Document version metadata

Get metadata (uid, content shas, version sha, tags) for a specific API document version.

| Direction | Type |
| --- | --- |
| Response | [`RegistryListApiDocumentVersionMetadataResponse`](./src/types/registry_list_api_document_version_metadata_response.py) |

```python
registry = client.registry.list_api_document_version_metadata(
    namespace="namespace",
    slug="slug",
    semver="semver",
)
```

### Create API Document version

Create a new API document version.

| Direction | Type |
| --- | --- |
| Request | [`RegistryCreateApiDocumentVersionParams`](./src/types/registry_create_api_document_version_params.py) |
| Response | [`RegistryCreateApiDocumentVersionResponse`](./src/types/registry_create_api_document_version_response.py) |

```python
registry = client.registry.create_api_document_version(
    namespace="namespace",
    slug="slug",
    version="",
    document="",
    idempotency_key="",
)
```

### Add access group

Add an access group to an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryCreateApiDocumentAccessGroupParams`](./src/types/registry_create_api_document_access_group_params.py) |
| Response | [`RegistryCreateApiDocumentAccessGroupResponse`](./src/types/registry_create_api_document_access_group_response.py) |

```python
registry = client.registry.create_api_document_access_group(
    namespace="namespace",
    slug="slug",
    access_group_slug="",
    idempotency_key="",
)
```

### Remove access group

Remove an access group from an API document.

| Direction | Type |
| --- | --- |
| Request | [`RegistryDeleteApiDocumentAccessGroupParams`](./src/types/registry_delete_api_document_access_group_params.py) |
| Response | [`RegistryDeleteApiDocumentAccessGroupResponse`](./src/types/registry_delete_api_document_access_group_response.py) |

```python
registry = client.registry.delete_api_document_access_group(
    namespace="namespace",
    slug="slug",
    access_group_slug="",
    idempotency_key="",
)
```

## `Schemas`

### List all shared components

List schemas in a namespace.

| Direction | Type |
| --- | --- |
| Response | [`SchemaListResponse`](./src/types/schema_list_response.py) |

```python
schema = client.schemas.list(
    namespace="namespace",
)
```

### Create a shared component

Create a schema in a namespace.

| Direction | Type |
| --- | --- |
| Request | [`SchemaCreateParams`](./src/types/schema_create_params.py) |
| Response | [`SchemaCreateResponse`](./src/types/schema_create_response.py) |

```python
schema = client.schemas.create(
    namespace="namespace",
    title="",
    version="",
    slug="",
    document="",
    idempotency_key="",
)
```

### Update shared component metadata

Update schema metadata.

| Direction | Type |
| --- | --- |
| Request | [`SchemaUpdateParams`](./src/types/schema_update_params.py) |
| Response | [`SchemaUpdateResponse`](./src/types/schema_update_response.py) |

```python
schema = client.schemas.update(
    namespace="namespace",
    slug="slug",
    idempotency_key="",
)
```

### Delete a shared component

Delete a schema and all related versions.

| Direction | Type |
| --- | --- |
| Response | [`SchemaDeleteResponse`](./src/types/schema_delete_response.py) |

```python
schema = client.schemas.delete(
    namespace="namespace",
    slug="slug",
    idempotency_key="",
)
```

### `Schemas Version`

#### Get a shared component document

Get a specific schema version document.

| Direction | Type |
| --- | --- |
| Response | [`VersionRetrieveSchemaResponse`](./src/types/schemas/version_retrieve_schema_response.py) |

```python
version = client.schemas.version.retrieve_schema(
    namespace="namespace",
    slug="slug",
    semver="semver",
)
```

#### Delete a shared component version

Delete a schema version.

| Direction | Type |
| --- | --- |
| Response | [`VersionDeleteSchemaResponse`](./src/types/schemas/version_delete_schema_response.py) |

```python
version = client.schemas.version.delete_schema(
    namespace="namespace",
    slug="slug",
    semver="semver",
    idempotency_key="",
)
```

#### Create a shared component version

Create a schema version.

| Direction | Type |
| --- | --- |
| Request | [`VersionCreateSchemaParams`](./src/types/schemas/version_create_schema_params.py) |
| Response | [`VersionCreateSchemaResponse`](./src/types/schemas/version_create_schema_response.py) |

```python
version = client.schemas.version.create_schema(
    namespace="namespace",
    slug="slug",
    version="",
    document="",
    idempotency_key="",
)
```

### `Schemas AccessGroup`

#### Add shared component access group

Add an access group to a schema.

| Direction | Type |
| --- | --- |
| Request | [`AccessGroupCreateSchemaParams`](./src/types/schemas/access_group_create_schema_params.py) |
| Response | [`AccessGroupCreateSchemaResponse`](./src/types/schemas/access_group_create_schema_response.py) |

```python
access_group = client.schemas.access_group.create_schema(
    namespace="namespace",
    slug="slug",
    access_group_slug="",
    idempotency_key="",
)
```

#### Remove shared component access group

Remove an access group from a schema.

| Direction | Type |
| --- | --- |
| Request | [`AccessGroupDeleteSchemaParams`](./src/types/schemas/access_group_delete_schema_params.py) |
| Response | [`AccessGroupDeleteSchemaResponse`](./src/types/schemas/access_group_delete_schema_response.py) |

```python
access_group = client.schemas.access_group.delete_schema(
    namespace="namespace",
    slug="slug",
    access_group_slug="",
    idempotency_key="",
)
```

## `LoginPortals`

### Get a login portal

Get a login portal by slug.

| Direction | Type |
| --- | --- |
| Response | [`LoginPortalRetrieveResponse`](./src/types/login_portal_retrieve_response.py) |

```python
login_portal = client.login_portals.retrieve(
    slug="slug",
)
```

### Update portal metadata

Update metadata for a login portal.

| Direction | Type |
| --- | --- |
| Request | [`LoginPortalUpdateParams`](./src/types/login_portal_update_params.py) |
| Response | [`LoginPortalUpdateResponse`](./src/types/login_portal_update_response.py) |

```python
login_portal = client.login_portals.update(
    slug="slug",
    idempotency_key="",
)
```

### Delete a login portal

Delete a login portal.

| Direction | Type |
| --- | --- |
| Response | [`LoginPortalDeleteResponse`](./src/types/login_portal_delete_response.py) |

```python
login_portal = client.login_portals.delete(
    slug="slug",
    idempotency_key="",
)
```

### Create a portal

Create a login portal for the current team.

| Direction | Type |
| --- | --- |
| Request | [`LoginPortalCreateParams`](./src/types/login_portal_create_params.py) |
| Response | [`LoginPortalCreateResponse`](./src/types/login_portal_create_response.py) |

```python
login_portal = client.login_portals.create(
    title="",
    slug="",
    email={"logo": "", "logo_size": "100", "button_text": "Login", "message": "Click to access private documentation hosted by scalar.com", "title": "Private Docs", "main_color": "#2a2f45", "main_background": "#f6f6f6", "card_color": "2a2f45", "card_background": "#fff", "button_color": "#fff", "button_background": "#0f0f0f"},
    page={"title": "Scalar Private Docs", "description": "Login to access your documentation", "head": "", "script": "", "theme": "", "company_name": "", "logo": "", "logo_url": "", "favicon": "", "terms_link": "", "privacy_link": "", "form_title": "Scalar Private Docs", "form_description": "Login to access your documentation", "form_image": ""},
    idempotency_key="",
)
```

### List all portals

List all login portals for the current team.

| Direction | Type |
| --- | --- |
| Response | [`LoginPortalListResponse`](./src/types/login_portal_list_response.py) |

```python
login_portal = client.login_portals.list()
```

## `Rules`

### List all rules

List all rulesets in a namespace.

| Direction | Type |
| --- | --- |
| Response | [`RuleListRulesetsResponse`](./src/types/rule_list_rulesets_response.py) |

```python
rule = client.rules.list_rulesets(
    namespace="namespace",
)
```

### Create a rule

Create a rule in a namespace.

| Direction | Type |
| --- | --- |
| Request | [`RuleCreateRulesetParams`](./src/types/rule_create_ruleset_params.py) |
| Response | [`RuleCreateRulesetResponse`](./src/types/rule_create_ruleset_response.py) |

```python
rule = client.rules.create_ruleset(
    namespace="namespace",
    title="",
    slug="",
    document="",
    idempotency_key="",
)
```

### Update rule metadata

Update rule metadata by slug.

| Direction | Type |
| --- | --- |
| Request | [`RuleUpdateRulesetParams`](./src/types/rule_update_ruleset_params.py) |
| Response | [`RuleUpdateRulesetResponse`](./src/types/rule_update_ruleset_response.py) |

```python
rule = client.rules.update_ruleset(
    namespace="namespace",
    slug="slug",
    idempotency_key="",
)
```

### Delete a rule

Delete a rule by slug.

| Direction | Type |
| --- | --- |
| Response | [`RuleDeleteRulesetResponse`](./src/types/rule_delete_ruleset_response.py) |

```python
rule = client.rules.delete_ruleset(
    namespace="namespace",
    slug="slug",
    idempotency_key="",
)
```

### Get a rule

Get a rule document by slug.

| Direction | Type |
| --- | --- |
| Response | [`RuleRetrieveRulesetDocumentResponse`](./src/types/rule_retrieve_ruleset_document_response.py) |

```python
rule = client.rules.retrieve_ruleset_document(
    namespace="namespace",
    slug="slug",
)
```

### Add rule access group

Grant an access group to a rule.

| Direction | Type |
| --- | --- |
| Request | [`RuleCreateRulesetAccessGroupParams`](./src/types/rule_create_ruleset_access_group_params.py) |
| Response | [`RuleCreateRulesetAccessGroupResponse`](./src/types/rule_create_ruleset_access_group_response.py) |

```python
rule = client.rules.create_ruleset_access_group(
    namespace="namespace",
    slug="slug",
    access_group_slug="",
    idempotency_key="",
)
```

### Remove rule access group

Remove an access group from a rule.

| Direction | Type |
| --- | --- |
| Request | [`RuleDeleteRulesetAccessGroupParams`](./src/types/rule_delete_ruleset_access_group_params.py) |
| Response | [`RuleDeleteRulesetAccessGroupResponse`](./src/types/rule_delete_ruleset_access_group_response.py) |

```python
rule = client.rules.delete_ruleset_access_group(
    namespace="namespace",
    slug="slug",
    access_group_slug="",
    idempotency_key="",
)
```

## `Themes`

### List all themes

List all team themes.

| Direction | Type |
| --- | --- |
| Response | [`ThemeListResponse`](./src/types/theme_list_response.py) |

```python
theme = client.themes.list()
```

### Create a theme

Create a team theme.

| Direction | Type |
| --- | --- |
| Request | [`ThemeCreateParams`](./src/types/theme_create_params.py) |
| Response | [`ThemeCreateResponse`](./src/types/theme_create_response.py) |

```python
theme = client.themes.create(
    name="",
    slug="",
    document="",
    idempotency_key="",
)
```

### Update theme metadata

Update theme metadata.

| Direction | Type |
| --- | --- |
| Request | [`ThemeUpdateParams`](./src/types/theme_update_params.py) |
| Response | [`ThemeUpdateResponse`](./src/types/theme_update_response.py) |

```python
theme = client.themes.update(
    slug="slug",
    idempotency_key="",
)
```

### Update theme document

Replace the theme document.

| Direction | Type |
| --- | --- |
| Request | [`ThemeReplaceDocumentParams`](./src/types/theme_replace_document_params.py) |
| Response | [`ThemeReplaceDocumentResponse`](./src/types/theme_replace_document_response.py) |

```python
theme = client.themes.replace_document(
    slug="slug",
    document="",
    idempotency_key="",
)
```

### Delete a theme

Delete a theme by slug.

| Direction | Type |
| --- | --- |
| Response | [`ThemeDeleteResponse`](./src/types/theme_delete_response.py) |

```python
theme = client.themes.delete(
    slug="slug",
    idempotency_key="",
)
```

### Get a theme

Get the theme document by slug.

| Direction | Type |
| --- | --- |
| Response | [`ThemeRetrieveResponse`](./src/types/theme_retrieve_response.py) |

```python
theme = client.themes.retrieve(
    slug="slug",
)
```

## `Teams`

### List teams

List all available teams

| Direction | Type |
| --- | --- |
| Response | [`TeamListResponse`](./src/types/team_list_response.py) |

```python
team = client.teams.list()
```

## `ScalarDocs`

### List all projects

List all guide projects.

| Direction | Type |
| --- | --- |
| Response | [`ScalarDocListGuidesResponse`](./src/types/scalar_doc_list_guides_response.py) |

```python
scalar_doc = client.scalar_docs.list_guides()
```

### Create a project

Create a guide project.

| Direction | Type |
| --- | --- |
| Request | [`ScalarDocCreateGuideParams`](./src/types/scalar_doc_create_guide_params.py) |
| Response | [`ScalarDocCreateGuideResponse`](./src/types/scalar_doc_create_guide_response.py) |

```python
scalar_doc = client.scalar_docs.create_guide(
    name="",
    is_private=False,
    allowed_users=[],
    allowed_domains=[],
    idempotency_key="",
)
```

### Publish a project

Start a new publish process.

| Direction | Type |
| --- | --- |
| Response | [`ScalarDocPublishGuideResponse`](./src/types/scalar_doc_publish_guide_response.py) |

```python
scalar_doc = client.scalar_docs.publish_guide(
    slug="slug",
    idempotency_key="",
)
```

## `Namespaces`

### List namespaces

Get all namespaces for the current team

| Direction | Type |
| --- | --- |
| Response | [`NamespaceListResponse`](./src/types/namespace_list_response.py) |

```python
namespace = client.namespaces.list()
```

## `Authentication`

### Exchange token

Exchange an API key for an access token.

| Direction | Type |
| --- | --- |
| Request | [`AuthenticationExchangePersonalTokenParams`](./src/types/authentication_exchange_personal_token_params.py) |
| Response | [`AuthenticationExchangePersonalTokenResponse`](./src/types/authentication_exchange_personal_token_response.py) |

```python
authentication = client.authentication.exchange_personal_token(
    personal_token="",
    idempotency_key="",
)
```

### Get current user

Get the authenticated user, including their available teams and theme.

| Direction | Type |
| --- | --- |
| Response | [`AuthenticationListCurrentUserResponse`](./src/types/authentication_list_current_user_response.py) |

```python
authentication = client.authentication.list_current_user()
```
