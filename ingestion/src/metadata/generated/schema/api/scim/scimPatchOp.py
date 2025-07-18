# generated by datamodel-codegen:
#   filename:  api/scim/scimPatchOp.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import ConfigDict

from metadata.ingestion.models.custom_pydantic import BaseModel


class Op(Enum):
    add = 'add'
    replace = 'replace'
    remove = 'remove'


class Operation(BaseModel):
    op: Op
    path: Optional[str] = None
    value: Optional[Union[Dict[str, Any], List[Any], str, bool, float]] = None


class ScimPatchOp(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    schemas: List[str]
    Operations: List[Operation]
