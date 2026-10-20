from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-extract"
FIELDS = {"url": "string", "instructions": "string", "settings_country_code": "string", "settings_extract_schema_json": "string"}
GROUPS = {"settings": {"country_code": "string", "extract_schema_json": "string"}}


class RunExtractTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
