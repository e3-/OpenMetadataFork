# generated by datamodel-codegen:
#   filename:  governance/workflows/workflowDefinition.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...type import basic, entityHistory, entityReferenceList
from .elements import edge


class Type(Enum):
    eventBasedEntity = 'eventBasedEntity'
    noOp = 'noOp'
    periodicBatchEntity = 'periodicBatchEntity'


class WorkflowConfiguration(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    storeStageStatus: Annotated[
        bool,
        Field(
            description='If True, all the stage status will be stored in the database.',
            title='Storage Workflow Stage Status',
        ),
    ]


class Trigger(BaseModel):
    type: Optional[Type] = None


class WorkflowDefinition(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[
        Optional[basic.Uuid],
        Field(None, description='Unique identifier of this workflow definition.'),
    ]
    name: Annotated[
        basic.EntityName,
        Field(description='Name that identifies this workflow definition.'),
    ]
    displayName: Annotated[
        Optional[str],
        Field(
            None, description='Display Name that identifies this workflow definition.'
        ),
    ]
    fullyQualifiedName: Annotated[
        Optional[basic.FullyQualifiedEntityName],
        Field(None, description='FullyQualifiedName same as `name`.'),
    ]
    description: Annotated[
        basic.Markdown, Field(description='Description of the workflow definition.')
    ]
    owners: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(None, description='Owners of this workflow definition.'),
    ]
    version: Annotated[
        Optional[entityHistory.EntityVersion],
        Field(None, description='Metadata version of the entity.'),
    ]
    updatedAt: Annotated[
        Optional[basic.Timestamp],
        Field(
            None,
            description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
        ),
    ]
    updatedBy: Annotated[
        Optional[str], Field(None, description='User who made the update.')
    ]
    href: Annotated[
        Optional[basic.Href],
        Field(None, description='Link to the resource corresponding to this entity.'),
    ]
    changeDescription: Annotated[
        Optional[entityHistory.ChangeDescription],
        Field(None, description='Change that lead to this version of the entity.'),
    ]
    incrementalChangeDescription: Annotated[
        Optional[entityHistory.ChangeDescription],
        Field(None, description='Change that lead to this version of the entity.'),
    ]
    deleted: Annotated[
        Optional[bool],
        Field(
            False, description='When `true` indicates the entity has been soft deleted.'
        ),
    ]
    deployed: Annotated[
        Optional[bool],
        Field(None, description='When `true` indicates the workflow is deployed.'),
    ]
    config: Optional[WorkflowConfiguration] = None
    trigger: Annotated[Optional[Trigger], Field(None, description='Workflow Trigger.')]
    nodes: Annotated[
        Optional[List[Dict[str, Any]]],
        Field(None, description='List of nodes used on the workflow.'),
    ]
    edges: Annotated[
        Optional[List[edge.EdgeDefinition]],
        Field(
            None,
            description='List of edges that connect the workflow elements and guide its flow.',
        ),
    ]
