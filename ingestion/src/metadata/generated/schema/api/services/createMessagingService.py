# generated by datamodel-codegen:
#   filename:  api/services/createMessagingService.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...entity.services import messagingService
from ...type import basic, entityReference, entityReferenceList, tagLabel


class CreateMessagingServiceRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[
        basic.EntityName,
        Field(description='Name that identifies the this entity instance uniquely'),
    ]
    displayName: Annotated[
        Optional[str],
        Field(
            None,
            description='Display Name that identifies this messaging service. It could be title or label from the source services.',
        ),
    ]
    description: Annotated[
        Optional[basic.Markdown],
        Field(None, description='Description of messaging service entity.'),
    ]
    serviceType: messagingService.MessagingServiceType
    connection: Optional[messagingService.MessagingConnection] = None
    tags: Annotated[
        Optional[List[tagLabel.TagLabel]],
        Field(None, description='Tags for this Messaging Service.'),
    ]
    owners: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(None, description='Owners of this messaging service.'),
    ]
    dataProducts: Annotated[
        Optional[List[basic.FullyQualifiedEntityName]],
        Field(
            None,
            description='List of fully qualified names of data products this entity is part of.',
        ),
    ]
    domain: Annotated[
        Optional[str],
        Field(
            None,
            description='Fully qualified name of the domain the Messaging Service belongs to.',
        ),
    ]
    ingestionRunner: Annotated[
        Optional[entityReference.EntityReference],
        Field(
            None,
            description='The ingestion agent responsible for executing the ingestion pipeline.',
        ),
    ]
