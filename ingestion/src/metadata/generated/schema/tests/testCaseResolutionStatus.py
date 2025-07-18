# generated by datamodel-codegen:
#   filename:  tests/testCaseResolutionStatus.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..type import basic, entityReference
from . import assigned, resolved


class TestCaseResolutionStatusTypes(Enum):
    New = 'New'
    Ack = 'Ack'
    Assigned = 'Assigned'
    Resolved = 'Resolved'


class Severities(Enum):
    Severity1 = 'Severity1'
    Severity2 = 'Severity2'
    Severity3 = 'Severity3'
    Severity4 = 'Severity4'
    Severity5 = 'Severity5'


class Metric(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[Optional[str], Field(None, description='Name of the metric.')]
    value: Annotated[Optional[float], Field(None, description='Value of the metric.')]


class TestCaseResolutionStatus(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[
        Optional[basic.Uuid],
        Field(None, description='Unique identifier of this failure instance'),
    ]
    stateId: Annotated[
        Optional[basic.Uuid],
        Field(
            None,
            description='Sequence ID for a failure status. Statuses belonging to the same sequence will have the same ID. Unique across a failure cycle, i.e. new -> ack -> ... -> resolved.',
        ),
    ]
    timestamp: Annotated[
        Optional[basic.Timestamp],
        Field(None, description='Timestamp on which the failure was created.'),
    ]
    testCaseResolutionStatusType: Annotated[
        TestCaseResolutionStatusTypes,
        Field(description='Status of Test Case Acknowledgement.'),
    ]
    testCaseResolutionStatusDetails: Annotated[
        Optional[Union[assigned.Assigned, resolved.Resolved]],
        Field(None, description='Details of the test case failure status.'),
    ]
    updatedBy: Annotated[
        Optional[entityReference.EntityReference],
        Field(None, description='User who updated the test case failure status.'),
    ]
    updatedAt: Annotated[
        Optional[basic.Timestamp],
        Field(None, description='Time when test case resolution was updated.'),
    ]
    testCaseReference: Annotated[
        Optional[entityReference.EntityReference],
        Field(None, description='Test case reference'),
    ]
    severity: Annotated[
        Optional[Severities],
        Field(
            None,
            description='Severity failure for the test associated with the resolution.',
        ),
    ]
    metrics: Annotated[
        Optional[List[Metric]],
        Field(
            None,
            description='List of metrics associated with the test case resolution.',
        ),
    ]
