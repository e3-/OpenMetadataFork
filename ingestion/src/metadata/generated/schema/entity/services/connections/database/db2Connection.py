# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/db2Connection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from .....type import filterPattern
from .. import connectionBasicType


class Db2Type(Enum):
    Db2 = 'Db2'


class Db2Scheme(Enum):
    db2_ibm_db = 'db2+ibm_db'
    ibmi = 'ibmi'


class Db2Connection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[Db2Type],
        Field(Db2Type.Db2, description='Service Type', title='Service Type'),
    ]
    scheme: Annotated[
        Optional[Db2Scheme],
        Field(
            Db2Scheme.db2_ibm_db,
            description='SQLAlchemy driver scheme options.',
            title='Connection Scheme',
        ),
    ]
    username: Annotated[
        str,
        Field(
            description='Username to connect to DB2. This user should have privileges to read all the metadata in DB2.',
            title='Username',
        ),
    ]
    password: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='Password to connect to DB2.', title='Password'),
    ]
    hostPort: Annotated[
        str,
        Field(description='Host and port of the DB2 service.', title='Host and Port'),
    ]
    database: Annotated[
        str, Field(description='Database of the data source.', title='database')
    ]
    licenseFileName: Annotated[
        Optional[str],
        Field(
            None,
            description='License file name to connect to DB2.',
            title='License File Name',
        ),
    ]
    license: Annotated[
        Optional[str],
        Field(None, description='License to connect to DB2.', title='License'),
    ]
    clidriverVersion: Annotated[
        Optional[str],
        Field(
            None,
            description='CLI Driver version to connect to DB2. If not provided, the latest version will be used.',
            title='CLI Driver Version',
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
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    supportsProfiler: Annotated[
        Optional[connectionBasicType.SupportsProfiler],
        Field(None, title='Supports Profiler'),
    ]
    supportsDatabase: Annotated[
        Optional[connectionBasicType.SupportsDatabase],
        Field(None, title='Supports Database'),
    ]
    supportsQueryComment: Annotated[
        Optional[connectionBasicType.SupportsQueryComment],
        Field(None, title='Supports Query Comment'),
    ]
    sampleDataStorageConfig: Annotated[
        Optional[connectionBasicType.SampleDataStorageConfig],
        Field(None, title='Storage Config for Sample Data'),
    ]
    supportsViewLineageExtraction: Optional[
        connectionBasicType.SupportsViewLineageExtraction
    ] = None
