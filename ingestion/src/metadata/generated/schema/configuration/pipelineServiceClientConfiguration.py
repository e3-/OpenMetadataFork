# generated by datamodel-codegen:
#   filename:  configuration/pipelineServiceClientConfiguration.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..entity.services.connections.metadata import openMetadataConnection
from ..security.secrets import secretsManagerClientLoader
from ..security.ssl import verifySSLConfig
from . import authConfig


class PipelineServiceClientConfiguration(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    enabled: Annotated[
        Optional[bool],
        Field(
            True,
            description='Flags if the ingestion from the OpenMetadata UI is enabled. If ingesting externally, we can set this value to false to not check the Pipeline Service Client component health.',
        ),
    ]
    className: Annotated[
        str, Field(description='Class Name for the Pipeline Service Client.')
    ]
    apiEndpoint: Annotated[
        str,
        Field(
            description='External API root to interact with the Pipeline Service Client'
        ),
    ]
    hostIp: Annotated[
        Optional[str],
        Field(
            None,
            description='Pipeline Service Client host IP that will be used to connect to the sources.',
        ),
    ]
    healthCheckInterval: Annotated[
        Optional[int],
        Field(
            300,
            description='Interval in seconds that the server will use to check the /status of the pipelineServiceClient and flag any errors in a Prometheus metric `pipelineServiceClientStatus.counter`.',
        ),
    ]
    ingestionIpInfoEnabled: Annotated[
        Optional[bool],
        Field(
            False,
            description='Enable or disable the API that fetches the public IP running the ingestion process.',
        ),
    ]
    metadataApiEndpoint: Annotated[
        str,
        Field(description='Metadata api endpoint, e.g., `http://localhost:8585/api`'),
    ]
    verifySSL: Annotated[
        Optional[verifySSLConfig.VerifySSL],
        Field(
            verifySSLConfig.VerifySSL.no_ssl,
            description='Client SSL verification policy when connecting to the OpenMetadata server: no-ssl, ignore, validate.',
        ),
    ]
    sslConfig: Annotated[
        Optional[verifySSLConfig.SslConfig],
        Field(
            None,
            description='OpenMetadata Client SSL configuration. This SSL information is about the OpenMetadata server. It will be picked up from the pipelineServiceClient to use/ignore SSL when connecting to the OpenMetadata server.',
        ),
    ]
    secretsManagerLoader: Optional[
        secretsManagerClientLoader.SecretsManagerClientLoader
    ] = secretsManagerClientLoader.SecretsManagerClientLoader.noop
    authProvider: Annotated[
        Optional[openMetadataConnection.AuthProvider],
        Field(
            openMetadataConnection.AuthProvider.basic,
            description='Auth Provider with which OpenMetadata service configured with.',
        ),
    ]
    authConfig: Annotated[
        Optional[authConfig.AuthConfiguration],
        Field(None, description='Auth Provider Configuration.'),
    ]
    parameters: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description='Additional parameters to initialize the PipelineServiceClient.',
        ),
    ]
