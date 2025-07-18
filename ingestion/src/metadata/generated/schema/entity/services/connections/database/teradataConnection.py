# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/teradataConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from .....type import filterPattern
from .. import connectionBasicType


class Logmech(Enum):
    TD2 = 'TD2'
    LDAP = 'LDAP'
    JWT = 'JWT'
    KRB5 = 'KRB5'
    CUSTOM = 'CUSTOM'
    TDNEGO = 'TDNEGO'


class Tmode(Enum):
    ANSI = 'ANSI'
    TERA = 'TERA'
    DEFAULT = 'DEFAULT'


class TeradataType(Enum):
    Teradata = 'Teradata'


class TeradataScheme(Enum):
    teradatasql = 'teradatasql'


class TeradataConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[TeradataType],
        Field(TeradataType.Teradata, description='Service Type', title='Service Type'),
    ]
    scheme: Annotated[
        Optional[TeradataScheme],
        Field(
            TeradataScheme.teradatasql,
            description='SQLAlchemy driver scheme options.',
            title='Connection Scheme',
        ),
    ]
    username: Annotated[
        str,
        Field(
            description='Username to connect to Teradata. This user should have privileges to read all the metadata in Teradata.',
            title='Username',
        ),
    ]
    password: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='Password to connect to Teradata.', title='Password'),
    ]
    logmech: Annotated[
        Optional[Logmech],
        Field(
            Logmech.TD2,
            description='Specifies the logon authentication method. Possible values are TD2 (the default), JWT, LDAP, KRB5 for Kerberos, or TDNEGO',
            title='LOGMECH',
        ),
    ]
    logdata: Annotated[
        Optional[str],
        Field(
            None,
            description='Specifies additional data needed by a logon mechanism, such as a secure token, Distinguished Name, or a domain/realm name. LOGDATA values are specific to each logon mechanism.',
            title='Extra data for the chosen logon authentication method (LOGDATA)',
        ),
    ]
    hostPort: Annotated[
        str,
        Field(
            description='Host and port of the Teradata service.', title='Host and Port'
        ),
    ]
    tmode: Annotated[
        Optional[Tmode],
        Field(
            Tmode.DEFAULT,
            description='Specifies the transaction mode for the connection',
            title='Transaction mode',
        ),
    ]
    account: Annotated[
        Optional[str],
        Field(
            None,
            description='Specifies an account string to override the default account string defined for the database user. Accounts are used by the database for workload management and resource usage monitoring.',
            title='Teradata Database account',
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
    sampleDataStorageConfig: Annotated[
        Optional[connectionBasicType.SampleDataStorageConfig],
        Field(None, title='Storage Config for Sample Data'),
    ]
    supportsViewLineageExtraction: Optional[
        connectionBasicType.SupportsViewLineageExtraction
    ] = None
