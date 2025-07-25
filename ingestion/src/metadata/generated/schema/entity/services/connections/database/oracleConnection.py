# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/oracleConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from .....type import filterPattern
from .. import connectionBasicType


class OracleType(Enum):
    Oracle = 'Oracle'


class OracleScheme(Enum):
    oracle_cx_oracle = 'oracle+cx_oracle'


class OracleDatabaseSchema(BaseModel):
    databaseSchema: Annotated[
        str,
        Field(
            description='databaseSchema of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single databaseSchema. When left blank, OpenMetadata Ingestion attempts to scan all the databaseSchema.',
            title='DatabaseSchema',
        ),
    ]


class OracleServiceName(BaseModel):
    oracleServiceName: Annotated[
        str,
        Field(
            description='The Oracle Service name is the TNS alias that you give when you remotely connect to your database.',
            title='Oracle Service Name',
        ),
    ]


class OracleTNSConnection(BaseModel):
    oracleTNSConnection: Annotated[
        str,
        Field(
            description='Pass the full constructed TNS string, e.g., (DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=myhost)(PORT=1530)))(CONNECT_DATA=(SID=MYSERVICENAME))).',
            title='Oracle TNS Connection String',
        ),
    ]


class OracleConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[OracleType],
        Field(OracleType.Oracle, description='Service Type', title='Service Type'),
    ]
    scheme: Annotated[
        Optional[OracleScheme],
        Field(
            OracleScheme.oracle_cx_oracle,
            description='SQLAlchemy driver scheme options.',
            title='Connection Scheme',
        ),
    ]
    username: Annotated[
        str,
        Field(
            description='Username to connect to Oracle. This user should have privileges to read all the metadata in Oracle.',
            title='Username',
        ),
    ]
    password: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='Password to connect to Oracle.', title='Password'),
    ]
    hostPort: Annotated[
        Optional[str],
        Field(
            None,
            description='Host and port of the Oracle service.',
            title='Host and Port',
        ),
    ]
    oracleConnectionType: Annotated[
        Union[OracleDatabaseSchema, OracleServiceName, OracleTNSConnection],
        Field(
            description='Connect with oracle by either passing service name or database schema name.',
            title='Oracle Connection Type',
        ),
    ]
    instantClientDirectory: Annotated[
        Optional[str],
        Field(
            '/instantclient',
            description='This directory will be used to set the LD_LIBRARY_PATH env variable. It is required if you need to enable thick connection mode. By default, we bring instant client 19 and point to /instantclient.',
            title='Oracle instant client directory',
        ),
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
            {'includes': [], 'excludes': ['^sys$', '^ctxsys$', '^dbsnmp$', '^outln$']},
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
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsLineageExtraction: Optional[
        connectionBasicType.SupportsLineageExtraction
    ] = None
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    supportsProfiler: Annotated[
        Optional[connectionBasicType.SupportsProfiler],
        Field(None, title='Supports Profiler'),
    ]
    supportsQueryComment: Annotated[
        Optional[connectionBasicType.SupportsQueryComment],
        Field(None, title='Supports Query Comment'),
    ]
    supportsDataDiff: Annotated[
        Optional[connectionBasicType.SupportsDataDiff],
        Field(None, title='Supports Data Diff Extraction.'),
    ]
    sampleDataStorageConfig: Annotated[
        Optional[connectionBasicType.SampleDataStorageConfig],
        Field(None, title='Storage Config for Sample Data'),
    ]
