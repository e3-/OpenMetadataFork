# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/salesforceConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from .....security.ssl import verifySSLConfig
from .....type import filterPattern
from .. import connectionBasicType


class SalesforceType(Enum):
    Salesforce = 'Salesforce'


class SalesforceConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[SalesforceType],
        Field(
            SalesforceType.Salesforce, description='Service Type', title='Service Type'
        ),
    ]
    username: Annotated[
        str,
        Field(
            description='Username to connect to the Salesforce. This user should have privileges to read all the metadata in Redshift.',
            title='Username',
        ),
    ]
    password: Annotated[
        Optional[CustomSecretStr],
        Field(
            None, description='Password to connect to the Salesforce.', title='Password'
        ),
    ]
    securityToken: Annotated[
        Optional[CustomSecretStr],
        Field(None, description='Salesforce Security Token.', title='Security Token'),
    ]
    organizationId: Annotated[
        Optional[str],
        Field(
            None,
            description='Salesforce Organization ID is the unique identifier for your Salesforce identity',
            title='Salesforce Organization ID',
        ),
    ]
    sobjectName: Annotated[
        Optional[str],
        Field(None, description='Salesforce Object Name.', title='Object Name'),
    ]
    databaseName: Annotated[
        Optional[str],
        Field(
            None,
            description='Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name.',
            title='Database Name',
        ),
    ]
    salesforceApiVersion: Annotated[
        Optional[str],
        Field(
            '42.0',
            description='API version of the Salesforce instance',
            title='Salesforce API Version',
        ),
    ]
    salesforceDomain: Annotated[
        Optional[str],
        Field(
            'login',
            description='Domain of Salesforce instance',
            title='Salesforce Domain',
        ),
    ]
    sslConfig: Annotated[
        Optional[verifySSLConfig.SslConfig],
        Field(
            None, description='SSL Configuration details.', title='SSL Configuration'
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
