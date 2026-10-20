from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-yandexmarket-categories-products"
FIELDS = {"category": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "condition": "select", "price_min": "number", "price_max": "number", "payment": "select", "high_rating": "boolean", "vendor_id": "number"}
GROUPS = {}


class RunYandexmarketCategoriesProductsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
