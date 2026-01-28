from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr

from logging import getLogger

logger = getLogger(__name__)

class Settings(BaseSettings):
    """
    Settings for configuring logging in the application.
    """

    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      extra="ignore",  # Ignore any extra fields not defined in the model
                                      )
    
    LLM_MODEL_NAME: str = Field(description="Name of the language model to use")
    GEMINI_API_KEY: SecretStr = Field(description="API key for Google services")

@lru_cache(maxsize=1)
def get_settings():
    logger.info("Loading settings from .env file")
    return Settings() 

settings = get_settings()
