from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-seedrs-campaigns-search"
FIELDS = {"search": "string", "max_items": "integer", "sort": "select", "trending_in": "string", "include_prereg": "boolean", "types": "array", "tax_eligibilities": "array", "sectors": "array", "business_types": "array", "tags": "array"}
GROUPS = {}


class RunSeedrsCampaignsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
