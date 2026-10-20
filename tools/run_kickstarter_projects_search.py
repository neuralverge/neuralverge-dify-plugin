from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-kickstarter-projects-search"
FIELDS = {"term": "string", "category": "select", "state": "select", "sort": "select", "raised": "select", "staff_picks": "boolean", "location_id": "integer", "max_items": "integer", "start_page": "integer", "goal_min": "integer", "goal_max": "integer", "pledged_min": "integer", "pledged_max": "integer", "raised_min": "integer", "raised_max": "integer"}
GROUPS = {}


class RunKickstarterProjectsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
