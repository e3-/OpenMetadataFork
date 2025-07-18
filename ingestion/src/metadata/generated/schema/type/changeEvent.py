# generated by datamodel-codegen:
#   filename:  type/changeEvent.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from . import basic, changeEventType, entityHistory


class ChangeEvent(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[basic.Uuid, Field(description='Unique identifier for the event.')]
    eventType: changeEventType.EventType
    entityType: Annotated[
        str,
        Field(
            description='Entity type that changed. Use the schema of this entity to process the entity attribute.'
        ),
    ]
    entityId: Annotated[
        basic.Uuid,
        Field(description='Identifier of entity that was modified by the operation.'),
    ]
    domain: Annotated[
        Optional[basic.Uuid],
        Field(
            None, description='Domain of the entity that was modified by the operation.'
        ),
    ]
    entityFullyQualifiedName: Annotated[
        Optional[str],
        Field(
            None,
            description='Fully Qualified Name of entity that was modified by the operation.',
        ),
    ]
    previousVersion: Annotated[
        Optional[entityHistory.EntityVersion],
        Field(
            None,
            description='Version of the entity before this change. Note that not all changes result in entity version change. When entity version is not changed, `previousVersion` is same as `currentVersion`.',
        ),
    ]
    currentVersion: Annotated[
        Optional[entityHistory.EntityVersion],
        Field(
            None,
            description='Current version of the entity after this change. Note that not all changes result in entity version change. When entity version is not changed, `previousVersion` is same as `currentVersion`.',
        ),
    ]
    userName: Annotated[
        Optional[str],
        Field(
            None, description='Name of the user whose activity resulted in the change.'
        ),
    ]
    timestamp: Annotated[
        basic.Timestamp,
        Field(
            description='Timestamp when the change was made in Unix epoch time milliseconds.'
        ),
    ]
    changeDescription: Annotated[
        Optional[entityHistory.ChangeDescription],
        Field(
            None,
            description='For `eventType` `entityUpdated` this field captures details about what fields were added/updated/deleted. For `eventType` `entityCreated` or `entityDeleted` this field is null.',
        ),
    ]
    incrementalChangeDescription: Annotated[
        Optional[entityHistory.ChangeDescription],
        Field(None, description='Change that lead to this version of the entity.'),
    ]
    entity: Annotated[
        Optional[Any],
        Field(
            None,
            description='For `eventType` `entityCreated`, this field captures JSON coded string of the entity using the schema corresponding to `entityType`.',
        ),
    ]
