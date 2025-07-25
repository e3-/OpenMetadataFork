# generated by datamodel-codegen:
#   filename:  entity/policies/accessControl/rule.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ....type import basic
from . import resourceDescriptor


class Effect(Enum):
    allow = 'allow'
    deny = 'deny'


class Rule(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[str, Field(description='Name of this Rule.')]
    fullyQualifiedName: Annotated[
        Optional[basic.FullyQualifiedEntityName],
        Field(
            None, description='FullyQualifiedName in the form `policyName.ruleName`.'
        ),
    ]
    description: Annotated[
        Optional[basic.Markdown], Field(None, description='Description of the rule.')
    ]
    effect: Effect
    operations: Annotated[
        List[resourceDescriptor.Operation],
        Field(
            description='List of operation names related to the `resources`. Use `*` to include all the operations.'
        ),
    ]
    resources: Annotated[
        List[str],
        Field(
            description='Resources/objects related to this rule. Resources are typically `entityTypes` such as `table`, `database`, etc. It also includes `non-entityType` resources such as `lineage`. Use `*` to include all the resources.'
        ),
    ]
    condition: Annotated[
        Optional[basic.Expression],
        Field(
            None,
            description='Expression in SpEL used for matching of a `Rule` based on entity, resource, and environmental attributes.',
        ),
    ]
