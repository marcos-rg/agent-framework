import pytest
from pydantic import SecretStr
from agent.core.settings import Settings
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def settings():
    """Session-scoped fixture that provides Settings instance for testing."""
    load_dotenv(override=True)  # Load .env file for test settings
    return Settings()
    
