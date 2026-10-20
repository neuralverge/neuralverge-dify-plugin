from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-indiehackers-products-search"
FIELDS = {"sort": "select", "category": "string", "business_model": "select", "monthly_revenue_min": "integer", "monthly_revenue_max": "integer", "max_items": "integer"}
GROUPS = {}


class RunIndiehackersProductsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
