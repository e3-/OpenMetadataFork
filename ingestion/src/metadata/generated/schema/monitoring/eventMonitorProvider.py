# generated by datamodel-codegen:
#   filename:  monitoring/eventMonitorProvider.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum


class EventMonitorProvider(Enum):
    cloudwatch = 'cloudwatch'
    prometheus = 'prometheus'
