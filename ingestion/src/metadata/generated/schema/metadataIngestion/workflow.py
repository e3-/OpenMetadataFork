# generated by datamodel-codegen:
#   filename:  metadataIngestion/workflow.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import ConfigDict, Field, RootModel
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..entity.services.connections import serviceConnection
from ..entity.services.connections.metadata import openMetadataConnection
from ..type import basic
from . import (
    apiServiceMetadataPipeline,
    applicationPipeline,
    dashboardServiceMetadataPipeline,
    databaseServiceAutoClassificationPipeline,
    databaseServiceMetadataPipeline,
    databaseServiceProfilerPipeline,
    databaseServiceQueryLineagePipeline,
    databaseServiceQueryUsagePipeline,
    dataInsightPipeline,
    dbtPipeline,
    messagingServiceMetadataPipeline,
    metadataToElasticSearchPipeline,
    mlmodelServiceMetadataPipeline,
    pipelineServiceMetadataPipeline,
    reverseIngestionPipeline,
    searchServiceMetadataPipeline,
    storageServiceMetadataPipeline,
    testSuitePipeline,
)


class Processor(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        str, Field(description='Type of processor component ex: pii-processor')
    ]
    config: Optional[basic.ComponentConfig] = None


class Stage(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[str, Field(description='Type of stage component ex: table-usage')]
    config: Optional[basic.ComponentConfig] = None


class Sink(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[str, Field(description='Type of sink component ex: metadata')]
    config: Optional[basic.ComponentConfig] = None


class BulkSink(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        str, Field(description='Type of BulkSink component ex: metadata-usage')
    ]
    config: Optional[basic.ComponentConfig] = None


class LogLevels(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'


class WorkflowConfig(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    loggerLevel: Optional[LogLevels] = LogLevels.INFO
    raiseOnError: Annotated[
        Optional[bool],
        Field(
            True,
            description='Control if we want to flag the workflow as failed if we encounter any processing errors.',
        ),
    ]
    successThreshold: Annotated[
        Optional[int],
        Field(
            90,
            description='The percentage of successfully processed records that must be achieved for the pipeline to be considered successful. Otherwise, the pipeline will be marked as failed.',
            ge=0,
            le=100,
            title='Success Threshold',
        ),
    ]
    openMetadataServerConfig: openMetadataConnection.OpenMetadataConnection
    config: Optional[basic.ComponentConfig] = None


class SourceConfig(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    config: Optional[
        Union[
            databaseServiceMetadataPipeline.DatabaseServiceMetadataPipeline,
            databaseServiceQueryUsagePipeline.DatabaseServiceQueryUsagePipeline,
            databaseServiceQueryLineagePipeline.DatabaseServiceQueryLineagePipeline,
            dashboardServiceMetadataPipeline.DashboardServiceMetadataPipeline,
            messagingServiceMetadataPipeline.MessagingServiceMetadataPipeline,
            databaseServiceProfilerPipeline.DatabaseServiceProfilerPipeline,
            databaseServiceAutoClassificationPipeline.DatabaseServiceAutoClassificationPipeline,
            pipelineServiceMetadataPipeline.PipelineServiceMetadataPipeline,
            mlmodelServiceMetadataPipeline.MlModelServiceMetadataPipeline,
            storageServiceMetadataPipeline.StorageServiceMetadataPipeline,
            searchServiceMetadataPipeline.SearchServiceMetadataPipeline,
            testSuitePipeline.TestSuitePipeline,
            metadataToElasticSearchPipeline.MetadataToElasticSearchPipeline,
            dataInsightPipeline.DataInsightPipeline,
            dbtPipeline.DbtPipeline,
            applicationPipeline.ApplicationPipeline,
            apiServiceMetadataPipeline.ApiServiceMetadataPipeline,
            reverseIngestionPipeline.ReverseIngestionPipeline,
        ]
    ] = None


class Source(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        str,
        Field(
            description='Type of the source connector ex: mysql, snowflake, tableau etc..'
        ),
    ]
    serviceName: Annotated[
        Optional[str],
        Field(
            None,
            description='Type of the source connector ex: mysql, snowflake, tableau etc..',
        ),
    ]
    serviceConnection: Annotated[
        Optional[serviceConnection.ServiceConnection],
        Field(
            None,
            description='Connection configuration for the source. ex: mysql , tableau connection.',
        ),
    ]
    sourceConfig: SourceConfig


class OpenMetadataWorkflowConfig(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    source: Source
    processor: Optional[Processor] = None
    sink: Optional[Sink] = None
    stage: Optional[Stage] = None
    bulkSink: Optional[BulkSink] = None
    workflowConfig: WorkflowConfig
    ingestionPipelineFQN: Annotated[
        Optional[str],
        Field(
            None,
            description='Fully qualified name of ingestion pipeline, used to identify the current ingestion pipeline',
        ),
    ]
    pipelineRunId: Annotated[
        Optional[basic.Uuid],
        Field(
            None,
            description='Unique identifier of pipeline run, used to identify the current pipeline run',
        ),
    ]


class MetadataWorkflow1(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[
        Optional[basic.Uuid],
        Field(None, description='Unique identifier that identifies this pipeline.'),
    ]
    name: Annotated[
        basic.EntityName,
        Field(description='Name that identifies this pipeline instance uniquely.'),
    ]
    openMetadataWorkflowConfig: Annotated[
        OpenMetadataWorkflowConfig,
        Field(description='OpenMetadata Ingestion Workflow Config.'),
    ]


class MetadataWorkflow2(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[
        Optional[basic.Uuid],
        Field(None, description='Unique identifier that identifies this pipeline.'),
    ]
    name: Annotated[
        basic.EntityName,
        Field(description='Name that identifies this pipeline instance uniquely.'),
    ]
    openMetadataWorkflowConfig: Annotated[
        OpenMetadataWorkflowConfig,
        Field(description='OpenMetadata Ingestion Workflow Config.'),
    ]


class MetadataWorkflow(RootModel[Union[MetadataWorkflow1, MetadataWorkflow2]]):
    root: Annotated[
        Union[MetadataWorkflow1, MetadataWorkflow2],
        Field(
            description='OpenMetadata Ingestion Framework definition.',
            title='MetadataWorkflow',
        ),
    ]
