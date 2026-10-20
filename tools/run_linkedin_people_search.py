from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-linkedin-people-search"
FIELDS = {"searchQuery": "string", "maxResults": "number", "startPage": "number", "scraperMode": "string", "locations": "array", "currentCompany": "array", "pastCompany": "array", "currentJobTitleFilter": "array", "pastJobTitle": "array", "yearsOfExperienceFilter": "array", "yearsAtCurrentCompanyFilter": "array", "seniorityLevelFilter": "array", "functionFilter": "array", "industryIds": "array", "firstNames": "array", "lastNames": "array", "companyHeadcountFilter": "array"}
GROUPS = {}


class RunLinkedinPeopleSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
