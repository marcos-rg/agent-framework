import pytest
from pydantic import SecretStr


@pytest.mark.unit
class TestSettings:
    """Tests for the Settings configuration."""

    def test_llm_model_name(self, settings):
        """Verify LLM_MODEL_NAME is correctly set."""
        assert isinstance(settings.LLM_MODEL_NAME, str)

    def test_gemini_api_key(self, settings):
        """Verify GEMINI_API_KEY is correctly set as SecretStr."""
        assert isinstance(settings.GEMINI_API_KEY, SecretStr)

    def test_llm_model_provider(self, settings):
        """Verify LLM_MODEL_PROVIDER is correctly set."""
        assert isinstance(settings.LLM_MODEL_PROVIDER, str)
        
