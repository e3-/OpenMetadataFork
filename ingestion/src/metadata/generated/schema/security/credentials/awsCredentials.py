# generated by datamodel-codegen:
#   filename:  security/credentials/awsCredentials.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr


class AWSCredentials(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    awsAccessKeyId: Annotated[
        Optional[str],
        Field(None, description='AWS Access key ID.', title='AWS Access Key ID'),
    ]
    awsSecretAccessKey: Annotated[
        Optional[CustomSecretStr],
        Field(
            None, description='AWS Secret Access Key.', title='AWS Secret Access Key'
        ),
    ]
    awsRegion: Annotated[str, Field(description='AWS Region', title='AWS Region')]
    awsSessionToken: Annotated[
        Optional[str],
        Field(None, description='AWS Session Token.', title='AWS Session Token'),
    ]
    endPointURL: Annotated[
        Optional[AnyUrl],
        Field(None, description='EndPoint URL for the AWS', title='Endpoint URL'),
    ]
    profileName: Annotated[
        Optional[str],
        Field(
            None,
            description='The name of a profile to use with the boto session.',
            title='Profile Name',
        ),
    ]
    assumeRoleArn: Annotated[
        Optional[str],
        Field(
            None,
            description='The Amazon Resource Name (ARN) of the role to assume. Required Field in case of Assume Role',
            title='Role Arn for Assume Role',
        ),
    ]
    assumeRoleSessionName: Annotated[
        Optional[str],
        Field(
            'OpenMetadataSession',
            description='An identifier for the assumed role session. Use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. Required Field in case of Assume Role',
            title='Role Session Name for Assume Role',
        ),
    ]
    assumeRoleSourceIdentity: Annotated[
        Optional[str],
        Field(
            None,
            description='The Amazon Resource Name (ARN) of the role to assume. Optional Field in case of Assume Role',
            title='Source Identity for Assume Role',
        ),
    ]
