from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-yahoo-auctions-sellers-reviews"
FIELDS = {"seller": "string", "max_items": "integer", "start_page": "integer", "role": "select", "rating": "select"}
GROUPS = {}


class RunYahooAuctionsSellersReviewsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
