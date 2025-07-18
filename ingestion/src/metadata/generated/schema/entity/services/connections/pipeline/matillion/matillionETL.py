# generated by datamodel-codegen:
#   filename:  entity/services/connections/pipeline/matillion/matillionETL.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from ......security.ssl import verifySSLConfig


class Type(Enum):
    MatillionETL = 'MatillionETL'


class MatillionEtlAuthConfig(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Optional[Type] = Type.MatillionETL
    hostPort: Annotated[str, Field(description='Matillion Host', title='Host')]
    username: Annotated[
        str,
        Field(
            description='Username to connect to the Matillion. This user should have privileges to read all the metadata in Matillion.',
            title='Username',
        ),
    ]
    password: Annotated[
        CustomSecretStr,
        Field(description='Password to connect to the Matillion.', title='Password'),
    ]
    sslConfig: Optional[verifySSLConfig.SslConfig] = None
