from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-yc-companies-search"
FIELDS = {"query": "string", "batches": "string", "industries": "string", "regions": "string", "team_size_min": "integer", "team_size_max": "integer", "sort_by": "select", "is_hiring": "boolean", "top_company": "boolean", "nonprofit": "boolean", "max_items": "integer", "start_page": "integer"}
GROUPS = {}


class RunYcCompaniesSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
