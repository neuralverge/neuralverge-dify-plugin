from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-aliexpress-product-search"
FIELDS = {"keyword": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "currency": "select", "min_price": "number", "max_price": "number", "language": "select", "country": "string", "ship_from": "string", "filters": "string", "free_shipping": "boolean", "choice": "boolean", "four_star_and_up": "boolean", "local_shipping": "boolean"}
GROUPS = {}


class RunAliexpressProductSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
