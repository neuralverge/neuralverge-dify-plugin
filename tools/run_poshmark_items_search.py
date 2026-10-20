from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-poshmark-items-search"
FIELDS = {"query": "string", "domain": "select", "max_items": "integer", "start_page": "integer", "sort": "select", "availability": "select", "department": "select", "condition": "select", "category": "string", "subcategory": "string", "brand": "string", "size": "string", "price_min": "number", "price_max": "number", "shipping": "select", "color": "array"}
GROUPS = {}


class RunPoshmarkItemsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
