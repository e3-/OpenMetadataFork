# generated by datamodel-codegen:
#   filename:  type/entityHistory.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import ConfigDict, Field, RootModel
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from . import changeSummaryMap


class EntityVersionHistory(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    entityType: Annotated[
        str,
        Field(
            description='Entity type, such as `database`, `table`, `dashboard`, for which this version history is produced.'
        ),
    ]
    versions: List


class EntityVersion(RootModel[float]):
    root: Annotated[
        float,
        Field(
            description='Metadata version of the entity in the form `Major.Minor`. First version always starts from `0.1` when the entity is created. When the backward compatible changes are made to the entity, only the `Minor` version is incremented - example `1.0` is changed to `1.1`. When backward incompatible changes are made the `Major` version is incremented - example `1.1` to `2.0`.',
            ge=0.1,
            multiple_of=0.1,
        ),
    ]


class FieldName(RootModel[str]):
    root: Annotated[str, Field(description='Name of the field of an entity.')]


class FieldChange(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[
        Optional[FieldName],
        Field(None, description='Name of the entity field that changed.'),
    ]
    oldValue: Annotated[
        Optional[Any],
        Field(
            None,
            description='Previous value of the field. Note that this is a JSON string and use the corresponding field type to deserialize it.',
        ),
    ]
    newValue: Annotated[
        Optional[Any],
        Field(
            None,
            description='New value of the field. Note that this is a JSON string and use the corresponding field type to deserialize it.',
        ),
    ]


class IncrementalChangeDescription(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    fieldsAdded: Annotated[
        Optional[List[FieldChange]],
        Field(None, description='Names of fields added during the version changes.'),
    ]
    fieldsUpdated: Annotated[
        Optional[List[FieldChange]],
        Field(
            None,
            description='Fields modified during the version changes with old and new values.',
        ),
    ]
    fieldsDeleted: Annotated[
        Optional[List[FieldChange]],
        Field(
            None,
            description='Fields deleted during the version changes with old value before deleted.',
        ),
    ]
    previousVersion: Annotated[
        Optional[EntityVersion],
        Field(
            None,
            description='When a change did not result in change, this could be same as the current version.',
        ),
    ]


class ChangeDescription(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    fieldsAdded: Annotated[
        Optional[List[FieldChange]],
        Field(None, description='Names of fields added during the version changes.'),
    ]
    fieldsUpdated: Annotated[
        Optional[List[FieldChange]],
        Field(
            None,
            description='Fields modified during the version changes with old and new values.',
        ),
    ]
    fieldsDeleted: Annotated[
        Optional[List[FieldChange]],
        Field(
            None,
            description='Fields deleted during the version changes with old value before deleted.',
        ),
    ]
    previousVersion: Annotated[
        Optional[EntityVersion],
        Field(
            None,
            description='When a change did not result in change, this could be same as the current version.',
        ),
    ]
    changeSummary: Optional[changeSummaryMap.ChangeSummaryModel] = None
