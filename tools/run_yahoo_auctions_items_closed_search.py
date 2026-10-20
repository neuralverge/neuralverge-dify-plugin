from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-yahoo-auctions-items-closed-search"
FIELDS = {"keyword": "string", "keyword_exclude": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "condition": "select", "price_min": "integer", "price_max": "integer", "category": "integer", "brand_id": "integer", "region": "select", "seller_type": "select", "free_shipping": "boolean", "has_image": "boolean"}
GROUPS = {}


class RunYahooAuctionsItemsClosedSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
