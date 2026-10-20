from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-indiegogo-campaigns-search"
FIELDS = {"term": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "creator_id": "integer", "tags": "string", "phases": "array", "benefits": "array", "player_counts": "array", "categories": "array"}
GROUPS = {}


class RunIndiegogoCampaignsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
