# generated by datamodel-codegen:
#   filename:  metadataIngestion/dbtPipeline.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..type import filterPattern
from .dbtconfig import (
    dbtAzureConfig,
    dbtCloudConfig,
    dbtGCSConfig,
    dbtHttpConfig,
    dbtLocalConfig,
    dbtS3Config,
)


class DbtConfigType(Enum):
    DBT = 'DBT'


class DbtPipeline(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[DbtConfigType], Field(DbtConfigType.DBT, description='Pipeline type')
    ]
    dbtConfigSource: Annotated[
        Union[
            dbtCloudConfig.DbtCloudConfig,
            dbtLocalConfig.DbtLocalConfig,
            dbtHttpConfig.DbtHttpConfig,
            dbtS3Config.DbtS3Config,
            dbtGCSConfig.DbtGcsConfig,
            dbtAzureConfig.DbtAzureConfig,
        ],
        Field(
            description='Available sources to fetch DBT catalog and manifest files.',
            title='DBT Configuration Source',
        ),
    ]
    searchAcrossDatabases: Annotated[
        Optional[bool],
        Field(
            False,
            description='Optional configuration to search across databases for tables or not',
        ),
    ]
    dbtUpdateDescriptions: Annotated[
        Optional[bool],
        Field(
            False,
            description='Optional configuration to update the description from DBT or not',
        ),
    ]
    dbtUpdateOwners: Annotated[
        Optional[bool],
        Field(
            False,
            description='Optional configuration to update the owners from DBT or not',
        ),
    ]
    includeTags: Annotated[
        Optional[bool],
        Field(True, description='Optional configuration to toggle the tags ingestion.'),
    ]
    dbtClassificationName: Annotated[
        Optional[str],
        Field(
            'dbtTags',
            description='Custom OpenMetadata Classification name for dbt tags.',
            title='dbt Classification Name',
        ),
    ]
    schemaFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only fetch tables or databases that matches the pattern.',
            title='Schema Filter Pattern',
        ),
    ]
    tableFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex exclude tables or databases that matches the pattern.',
            title='Table Filter Pattern',
        ),
    ]
    parsingTimeoutLimit: Annotated[
        Optional[int],
        Field(
            300,
            description='Configuration to set the timeout for parsing the query in seconds.',
            title='Parsing Timeout Limit (in sec.)',
        ),
    ]
    databaseFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only fetch databases that matches the pattern.',
            title='Database Filter Pattern',
        ),
    ]
    tagFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only fetch tags that matches the pattern.',
            title='Tag Filter Pattern',
        ),
    ]
