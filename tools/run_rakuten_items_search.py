from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-rakuten-items-search"
FIELDS = {"keyword": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "condition": "select", "price_min": "number", "price_max": "number", "genre_id": "number"}
GROUPS = {}


class RunRakutenItemsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
