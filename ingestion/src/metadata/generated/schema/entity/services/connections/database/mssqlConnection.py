# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/mssqlConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from .....type import filterPattern
from .. import connectionBasicType


class MssqlType(Enum):
    Mssql = 'Mssql'


class MssqlScheme(Enum):
    mssql_pyodbc = 'mssql+pyodbc'
    mssql_pytds = 'mssql+pytds'
    mssql_pymssql = 'mssql+pymssql'


class MssqlConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[MssqlType],
        Field(MssqlType.Mssql, description='Service Type', title='Service Type'),
    ]
    scheme: Annotated[
        Optional[MssqlScheme],
        Field(
            MssqlScheme.mssql_pytds,
            description='SQLAlchemy driver scheme options.',
            title='Connection Scheme',
        ),
    ]
    username: Annotated[
        Optional[str],
        Field(
            None,
            description='Username to connect to MSSQL. This user should have privileges to read all the metadata in MsSQL.',
            title='Username',
        ),
    ]
    password: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='Password to connect to MSSQL.', title='Password'),
    ]
    hostPort: Annotated[
        Optional[str],
        Field(
            None,
            description='Host and port of the MSSQL service.',
            title='Host and Port',
        ),
    ]
    database: Annotated[
        str,
        Field(
            description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank, OpenMetadata Ingestion attempts to scan all the databases.',
            title='Database',
        ),
    ]
    driver: Annotated[
        Optional[str],
        Field(
            'ODBC Driver 18 for SQL Server',
            description='ODBC driver version in case of pyodbc connection.',
            title='Driver',
        ),
    ]
    ingestAllDatabases: Annotated[
        Optional[bool],
        Field(
            False,
            description='Ingest data from all databases in Mssql. You can use databaseFilterPattern on top of this.',
            title='Ingest All Databases',
        ),
    ]
    schemaFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            {
                'includes': [],
                'excludes': ['^db_.*', '^guest$', '^information_schema$', '^sys$'],
            },
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
            {'includes': [], 'excludes': ['^msdb$', '^model$', '^tempdb$']},
            description='Regex to only include/exclude databases that matches the pattern.',
            title='Default Database Filter Pattern',
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
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsLineageExtraction: Optional[
        connectionBasicType.SupportsLineageExtraction
    ] = None
    sampleDataStorageConfig: Annotated[
        Optional[connectionBasicType.SampleDataStorageConfig],
        Field(None, title='Storage Config for Sample Data'),
    ]
    supportsQueryComment: Annotated[
        Optional[connectionBasicType.SupportsQueryComment],
        Field(None, title='Supports Query Comment'),
    ]
    supportsDataDiff: Annotated[
        Optional[connectionBasicType.SupportsDataDiff],
        Field(None, title='Supports Data Diff Extraction.'),
    ]
