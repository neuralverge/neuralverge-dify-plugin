from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from nv_client import call

ENDPOINT = "run-craigslist-postings-search"
FIELDS = {"area": "string", "keyword": "string", "category": "string", "max_items": "integer", "start_page": "integer", "subarea": "string", "sort": "select", "purveyor": "select", "min_price": "number", "max_price": "number", "condition": "array", "language": "array", "free": "boolean", "titles_only": "boolean", "has_image": "boolean", "posted_today": "boolean", "hide_duplicates": "boolean", "crypto_ok": "boolean", "delivery_available": "boolean", "postal": "string", "lat": "number", "lon": "number", "radius": "number", "make_model": "string", "min_auto_year": "number", "max_auto_year": "number", "min_auto_miles": "number", "max_auto_miles": "number", "min_monthly_payment": "number", "max_monthly_payment": "number", "transmission": "array", "drivetrain": "array", "fuel_type": "array", "title_status": "array", "body_type": "array", "paint": "array", "cylinders": "array", "min_engine_displacement_cc": "number", "max_engine_displacement_cc": "number", "street_legal": "boolean", "motorcycle_motor": "array", "motorcycle_type": "array", "min_boat_length": "number", "max_boat_length": "number", "min_year_manufactured": "number", "max_year_manufactured": "number", "boat_propulsion": "array", "boat_type": "array", "min_bedrooms": "number", "max_bedrooms": "number", "min_bathrooms": "number", "max_bathrooms": "number", "min_sqft": "number", "max_sqft": "number", "availability": "select", "rent_period": "array", "housing_type": "array", "laundry": "array", "parking": "array", "housing_features": "array", "employment_type": "array", "is_internship": "boolean", "is_nonprofit": "boolean", "is_telecommuting": "boolean", "is_paid": "select", "lost_or_found": "array", "event_types": "array"}
GROUPS = {}


class RunCraigslistPostingsSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield from call(self, ENDPOINT, FIELDS, GROUPS, tool_parameters)
