from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-olx-offers-search"
FIELDS = {"domain": "select", "keyword": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "condition": "select", "owner_type": "select", "category_id": "integer", "min_price": "number", "max_price": "number", "region_id": "integer", "city_id": "integer", "district_id": "integer", "distance": "integer", "user_id": "integer", "has_delivery": "boolean"}
GROUPS = {}


class RunOlxOffersSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
