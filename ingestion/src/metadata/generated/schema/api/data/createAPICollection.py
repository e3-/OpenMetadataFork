# generated by datamodel-codegen:
#   filename:  api/data/createAPICollection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...type import basic, entityReferenceList, lifeCycle, tagLabel


class CreateAPICollectionRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[
        basic.EntityName, Field(description='Name that identifies this API Collection.')
    ]
    displayName: Annotated[
        Optional[str],
        Field(
            None,
            description='Display Name that identifies this API Collection. It could be title or label from the source services',
        ),
    ]
    description: Annotated[
        Optional[basic.Markdown],
        Field(
            None,
            description='Description of the API Collection instance. What it has and how to use it.',
        ),
    ]
    endpointURL: Annotated[
        Optional[AnyUrl],
        Field(
            None,
            description='EndPoint URL for the API Collection. Capture the Root URL of the collection.',
            title='Endpoint URL',
        ),
    ]
    apiEndpoints: Annotated[
        Optional[List[basic.FullyQualifiedEntityName]],
        Field(
            None,
            description="All the API's fullyQualifiedNames included in this API Collection.",
        ),
    ]
    tags: Annotated[
        Optional[List[tagLabel.TagLabel]],
        Field(None, description='Tags for this API Collection'),
    ]
    owners: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(None, description='Owners of this API Collection'),
    ]
    service: Annotated[
        basic.FullyQualifiedEntityName,
        Field(
            description='Link to the API service fully qualified name where this API collection is hosted in'
        ),
    ]
    extension: Annotated[
        Optional[basic.EntityExtension],
        Field(
            None,
            description='Entity extension data with custom attributes added to the entity.',
        ),
    ]
    domain: Annotated[
        Optional[basic.FullyQualifiedEntityName],
        Field(
            None,
            description='Fully qualified name of the domain the API Collection belongs to.',
        ),
    ]
    dataProducts: Annotated[
        Optional[List[basic.FullyQualifiedEntityName]],
        Field(
            None,
            description='List of fully qualified names of data products this entity is part of.',
        ),
    ]
    lifeCycle: Annotated[
        Optional[lifeCycle.LifeCycle],
        Field(None, description='Life Cycle of the entity'),
    ]
    sourceHash: Annotated[
        Optional[str],
        Field(
            None, description='Source hash of the entity', max_length=32, min_length=1
        ),
    ]
