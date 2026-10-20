from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-vinted-products-search"
FIELDS = {"keyword": "string", "domain": "select", "order": "select", "max_items": "integer", "start_page": "integer", "price_from": "number", "price_to": "number", "currency": "string", "catalog_ids": "string", "brand_ids": "string", "size_ids": "string", "status_ids": "string", "color_ids": "string", "material_ids": "string"}
GROUPS = {}


class RunVintedProductsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
