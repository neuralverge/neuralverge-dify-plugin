from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from nv_client import check_api_key


class NeuralvergeProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        api_key = credentials.get("api_key")
        if not api_key:
            raise ToolProviderCredentialValidationError("API key is required.")
        try:
            check_api_key(api_key)
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
