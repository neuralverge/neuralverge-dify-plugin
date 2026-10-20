from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-hepsiburada-products-search"
FIELDS = {"keyword": "string", "max_items": "integer", "start_page": "integer", "sort": "select", "rating_min": "select", "brand": "string", "color": "select", "merchant": "string", "product_type": "string", "price_min": "number", "price_max": "number", "fast_delivery": "boolean", "discounted_only": "boolean", "with_photo_reviews": "boolean", "authorized_seller": "boolean", "recently_reviewed": "boolean", "advantageous_price": "boolean"}
GROUPS = {}


class RunHepsiburadaProductsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
