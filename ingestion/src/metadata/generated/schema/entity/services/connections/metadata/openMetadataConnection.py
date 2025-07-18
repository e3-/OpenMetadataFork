# generated by datamodel-codegen:
#   filename:  entity/services/connections/metadata/openMetadataConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, Optional

from pydantic import ConfigDict, Field, RootModel
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from .....security.client import openMetadataJWTClientConfig
from .....security.secrets import secretsManagerClientLoader, secretsManagerProvider
from .....security.ssl import verifySSLConfig
from .....type import basic, filterPattern
from .. import connectionBasicType


class ElasticsSearch(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[str, Field(description='Type of sink component ex: metadata')]
    config: Optional[basic.ComponentConfig] = None


class OpenmetadataType(Enum):
    OpenMetadata = 'OpenMetadata'


class ExtraHeaders(RootModel[Optional[Dict[str, str]]]):
    root: Optional[Dict[str, str]] = None


class AuthProvider(Enum):
    basic = 'basic'
    azure = 'azure'
    google = 'google'
    okta = 'okta'
    auth0 = 'auth0'
    aws_cognito = 'aws-cognito'
    custom_oidc = 'custom-oidc'
    ldap = 'ldap'
    saml = 'saml'
    openmetadata = 'openmetadata'


class OpenMetadataConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    clusterName: Annotated[
        Optional[str],
        Field(
            'openmetadata',
            description='Cluster name to differentiate OpenMetadata Server instance',
        ),
    ]
    type: Annotated[
        Optional[OpenmetadataType],
        Field(OpenmetadataType.OpenMetadata, description='Service Type'),
    ]
    hostPort: Annotated[
        str,
        Field(
            description='OpenMetadata Server Config. Must include API end point ex: http://localhost:8585/api'
        ),
    ]
    authProvider: Annotated[
        Optional[AuthProvider],
        Field(
            AuthProvider.basic,
            description='OpenMetadata Server Authentication Provider.',
        ),
    ]
    verifySSL: Annotated[
        Optional[verifySSLConfig.VerifySSL],
        Field(
            verifySSLConfig.VerifySSL.no_ssl,
            description='Flag to verify SSL Certificate for OpenMetadata Server.',
        ),
    ]
    sslConfig: Annotated[
        Optional[verifySSLConfig.SslConfig],
        Field(None, description='SSL Configuration for OpenMetadata Server'),
    ]
    securityConfig: Annotated[
        Optional[openMetadataJWTClientConfig.OpenMetadataJWTClientConfig],
        Field(None, description='OpenMetadata Client security configuration.'),
    ]
    secretsManagerProvider: Annotated[
        Optional[secretsManagerProvider.SecretsManagerProvider],
        Field(
            secretsManagerProvider.SecretsManagerProvider.db,
            description='Secrets Manager Provider for OpenMetadata Server.',
        ),
    ]
    secretsManagerLoader: Annotated[
        Optional[secretsManagerClientLoader.SecretsManagerClientLoader],
        Field(
            secretsManagerClientLoader.SecretsManagerClientLoader.noop,
            description='Secrets Manager Loader for the Pipeline Service Client.',
        ),
    ]
    apiVersion: Annotated[
        Optional[str],
        Field('v1', description='OpenMetadata server API version to use.'),
    ]
    includeTopics: Annotated[
        Optional[bool], Field(True, description='Include Topics for Indexing')
    ]
    includeTables: Annotated[
        Optional[bool], Field(True, description='Include Tables for Indexing')
    ]
    includeDashboards: Annotated[
        Optional[bool], Field(True, description='Include Dashboards for Indexing')
    ]
    includePipelines: Annotated[
        Optional[bool], Field(True, description='Include Pipelines for Indexing')
    ]
    includeMlModels: Annotated[
        Optional[bool], Field(True, description='Include MlModels for Indexing')
    ]
    includeUsers: Annotated[
        Optional[bool], Field(True, description='Include Users for Indexing')
    ]
    includeTeams: Annotated[
        Optional[bool], Field(True, description='Include Teams for Indexing')
    ]
    includeGlossaryTerms: Annotated[
        Optional[bool], Field(True, description='Include Glossary Terms for Indexing')
    ]
    includeTags: Annotated[
        Optional[bool], Field(True, description='Include Tags for Indexing')
    ]
    includePolicy: Annotated[
        Optional[bool], Field(True, description='Include Tags for Policy')
    ]
    includeMessagingServices: Annotated[
        Optional[bool],
        Field(True, description='Include Messaging Services for Indexing'),
    ]
    enableVersionValidation: Annotated[
        Optional[bool],
        Field(True, description='Validate Openmetadata Server & Client Version.'),
    ]
    includeDatabaseServices: Annotated[
        Optional[bool],
        Field(True, description='Include Database Services for Indexing'),
    ]
    includePipelineServices: Annotated[
        Optional[bool],
        Field(True, description='Include Pipeline Services for Indexing'),
    ]
    limitRecords: Annotated[
        Optional[int],
        Field(1000, description='Limit the number of records for Indexing.'),
    ]
    forceEntityOverwriting: Annotated[
        Optional[bool],
        Field(
            False,
            description='Force the overwriting of any entity during the ingestion.',
        ),
    ]
    storeServiceConnection: Annotated[
        Optional[bool],
        Field(
            True,
            description='If set to true, when creating a service during the ingestion we will store its Service Connection. Otherwise, the ingestion will create a bare service without connection details.',
        ),
    ]
    elasticsSearch: Annotated[
        Optional[ElasticsSearch],
        Field(
            None,
            description='Configuration for Sink Component in the OpenMetadata Ingestion Framework.',
        ),
    ]
    schemaFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only include/exclude schemas that matches the pattern.',
            title='Default Schema Filter Pattern',
        ),
    ]
    tableFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only include/exclude tables that matches the pattern.',
            title='Default Table Filter Pattern',
        ),
    ]
    databaseFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only include/exclude databases that matches the pattern.',
            title='Default Database Filter Pattern',
        ),
    ]
    supportsDataInsightExtraction: Annotated[
        Optional[connectionBasicType.SupportsDataInsightExtraction],
        Field(None, description='Flag to enable Data Insight Extraction'),
    ]
    supportsElasticSearchReindexingExtraction: Annotated[
        Optional[connectionBasicType.SupportsElasticSearchReindexingExtraction],
        Field(None, description='Flag to enable ElasticSearch Reindexing Extraction'),
    ]
    extraHeaders: Annotated[Optional[ExtraHeaders], Field(None, title='Extra Headers')]
