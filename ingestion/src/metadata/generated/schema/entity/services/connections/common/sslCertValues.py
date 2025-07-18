# generated by datamodel-codegen:
#   filename:  entity/services/connections/common/sslCertValues.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr


class SslCertificatesByValues(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    caCertValue: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='CA Certificate Value', title='CA Certificate Value'),
    ]
    clientCertValue: Annotated[
        Optional[CustomSecretStr],
        Field(
            None,
            description='Client Certificate Value',
            title='Client Certificate Value',
        ),
    ]
    privateKeyValue: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='Private Key Value', title='Private Key Value'),
    ]
    stagingDir: Annotated[
        Optional[str],
        Field(
            '/tmp/openmetadata-certs',
            description='Staging Directory Path',
            title='Staging Directory Path',
        ),
    ]
