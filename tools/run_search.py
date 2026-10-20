from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-search"
FIELDS = {"query": "string", "settings_country": "string", "settings_language": "string", "settings_max_results": "number"}
GROUPS = {"settings": {"country": "string", "language": "string", "max_results": "number"}}


class RunSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
