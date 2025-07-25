# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/dynamoDBConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from .....security.credentials import awsCredentials
from .....type import filterPattern
from .. import connectionBasicType


class DynamoDBType(Enum):
    DynamoDB = 'DynamoDB'


class DynamoDBConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[DynamoDBType],
        Field(DynamoDBType.DynamoDB, description='Service Type', title='Service Type'),
    ]
    awsConfig: Annotated[
        awsCredentials.AWSCredentials, Field(title='AWS Credentials Configuration')
    ]
    databaseName: Annotated[
        Optional[str],
        Field(
            None,
            description='Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name.',
            title='Database Name',
        ),
    ]
    connectionOptions: Annotated[
        Optional[connectionBasicType.ConnectionOptions],
        Field(None, title='Connection Options'),
    ]
    connectionArguments: Annotated[
        Optional[connectionBasicType.ConnectionArguments],
        Field(None, title='Connection Arguments'),
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
    supportsMetadataExtraction: Annotated[
        Optional[connectionBasicType.SupportsMetadataExtraction],
        Field(None, title='Supports Metadata Extraction'),
    ]
    supportsProfiler: Annotated[
        Optional[connectionBasicType.SupportsProfiler],
        Field(None, title='Supports Profiler'),
    ]
