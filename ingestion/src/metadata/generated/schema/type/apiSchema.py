# generated by datamodel-codegen:
#   filename:  type/apiSchema.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from . import schema


class APISchema(BaseModel):
    schemaType: Annotated[
        Optional[schema.SchemaType],
        Field(
            schema.SchemaType.JSON, description='Schema used for message serialization.'
        ),
    ]
    schemaFields: Annotated[
        Optional[List[schema.FieldModel]],
        Field([], description='Columns in this schema.'),
    ]
