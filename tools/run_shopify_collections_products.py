from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-shopify-collections-products"
FIELDS = {"store_domain": "string", "collection": "string", "max_items": "integer", "start_page": "integer"}
GROUPS = {}


class RunShopifyCollectionsProductsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
