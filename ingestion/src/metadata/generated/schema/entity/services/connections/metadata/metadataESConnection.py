# generated by datamodel-codegen:
#   filename:  entity/services/connections/metadata/metadataESConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from .....configuration import elasticSearchConfiguration
from .....system import eventPublisherJob
from .....type import filterPattern
from .. import connectionBasicType


class MetadataESType(Enum):
    MetadataES = 'MetadataES'


class MetadataESConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[MetadataESType],
        Field(MetadataESType.MetadataES, description='Service Type'),
    ]
    entities: Annotated[
        Optional[List[str]],
        Field(
            [
                'table',
                'topic',
                'dashboard',
                'pipeline',
                'mlmodel',
                'user',
                'team',
                'glossaryTerm',
                'tag',
                'entityReportData',
                'webAnalyticEntityViewReportData',
                'webAnalyticUserActivityReportData',
                'container',
                'query',
            ],
            description='List of entities that you need to reindex',
            title='Entities',
        ),
    ]
    recreateIndex: Annotated[Optional[bool], Field(True, title='Recreate Indexes')]
    runMode: Optional[eventPublisherJob.RunMode] = None
    searchIndexMappingLanguage: Annotated[
        Optional[elasticSearchConfiguration.SearchIndexMappingLanguage],
        Field(
            elasticSearchConfiguration.SearchIndexMappingLanguage.EN,
            description='Recreate Indexes with updated Language',
        ),
    ]
    batchSize: Annotated[
        Optional[int],
        Field(
            100,
            description='Maximum number of events sent in a batch (Default 100).',
            title='Batch Size',
        ),
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
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = None
