# generated by datamodel-codegen:
#   filename:  api/data/updateColumn.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...entity.data import table
from ...type import basic, tagLabel


class UpdateColumn(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    displayName: Annotated[
        Optional[str],
        Field(None, description='Display Name that identifies this column name.'),
    ]
    description: Annotated[
        Optional[basic.Markdown], Field(None, description='Description of the column.')
    ]
    tags: Annotated[
        Optional[List[tagLabel.TagLabel]],
        Field(
            None,
            description="Tags and glossary terms associated with the column. Use source: 'Classification' for classification tags and source: 'Glossary' for glossary terms. Provide an empty array to remove all tags. Note: Invalid or non-existent tags/glossary terms will result in a 404 error.",
        ),
    ]
    constraint: Annotated[
        Optional[table.Constraint],
        Field(
            None,
            description='Column level constraint. Only applicable to table columns, ignored for dashboard data model columns.',
        ),
    ]
    removeConstraint: Annotated[
        Optional[bool],
        Field(
            False,
            description="Set to true to remove the existing column constraint. Only applicable to table columns, ignored for dashboard data model columns. If both 'constraint' and 'removeConstraint' are provided, 'removeConstraint' takes precedence.",
        ),
    ]
