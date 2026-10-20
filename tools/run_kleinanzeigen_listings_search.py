from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-kleinanzeigen-listings-search"
FIELDS = {"keyword": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "condition": "select", "offer_type": "select", "seller_type": "select", "shipping": "select", "carrier": "select", "min_price": "number", "max_price": "number", "category_id": "string", "buy_now": "boolean"}
GROUPS = {}


class RunKleinanzeigenListingsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
