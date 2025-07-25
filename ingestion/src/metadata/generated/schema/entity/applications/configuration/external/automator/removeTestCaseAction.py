# generated by datamodel-codegen:
#   filename:  entity/applications/configuration/external/automator/removeTestCaseAction.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ......type import basic


class RemoveTestCaseActionType(Enum):
    RemoveTestCaseAction = 'RemoveTestCaseAction'


class RemoveTestCaseAction(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        RemoveTestCaseActionType,
        Field(description='Application Type', title='Application Type'),
    ]
    testCaseDefinitions: Annotated[
        Optional[List[basic.FullyQualifiedEntityName]],
        Field(None, description='Test Cases to remove'),
    ]
    applyToChildren: Annotated[
        Optional[List[basic.EntityName]],
        Field(
            None,
            description='Remove tests to the selected table columns',
            title='Apply to Children',
        ),
    ]
    removeAll: Annotated[
        Optional[bool],
        Field(False, description='Remove all test cases', title='Remove All'),
    ]
