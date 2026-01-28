from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
import logging

# Use basic logging here to avoid circular imports since logger module imports settings
logger = logging.getLogger("agent.settings")

class Settings(BaseSettings):
    """
    Settings for configuring logging in the application.
    """

    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      extra="ignore",  # Ignore any extra fields not defined in the model
                                      )
    
    LLM_MODEL_NAME: str = Field(description="Name of the language model to use")
    LLM_MODEL_PROVIDER: str = Field(description="Provider of the language model")
    API_KEY: SecretStr = Field(description="API key for Google services")

@lru_cache(maxsize=1)
def get_settings():
    logger.info("Loading settings from .env file")
    return Settings() 

settings = get_settings()
