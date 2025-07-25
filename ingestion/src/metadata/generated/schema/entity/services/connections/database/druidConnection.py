# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/druidConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from .....type import filterPattern
from .. import connectionBasicType


class DruidType(Enum):
    Druid = 'Druid'


class DruidScheme(Enum):
    druid = 'druid'


class DruidConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[DruidType],
        Field(DruidType.Druid, description='Service Type', title='Service Type'),
    ]
    scheme: Annotated[
        Optional[DruidScheme],
        Field(
            DruidScheme.druid,
            description='SQLAlchemy driver scheme options.',
            title='Connection Scheme',
        ),
    ]
    username: Annotated[
        Optional[str],
        Field(
            None,
            description='Username to connect to Druid. This user should have privileges to read all the metadata in Druid.',
            title='Username',
        ),
    ]
    password: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='Password to connect to Druid.', title='Password'),
    ]
    hostPort: Annotated[
        str,
        Field(description='Host and port of the Druid service.', title='Host and Port'),
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
    supportsQueryComment: Annotated[
        Optional[connectionBasicType.SupportsQueryComment],
        Field(None, title='Supports Query Comment'),
    ]
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    sampleDataStorageConfig: Annotated[
        Optional[connectionBasicType.SampleDataStorageConfig],
        Field(None, title='Storage Config for Sample Data'),
    ]
    supportsViewLineageExtraction: Optional[
        connectionBasicType.SupportsViewLineageExtraction
    ] = None
