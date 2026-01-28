from agent.core.settings import settings

from logging import getLogger

logger = getLogger(__name__)

def main():
    logger.info(f"Using LLM Model: {settings.LLM_MODEL_NAME}")
    # Here you would add the main logic of your agent application
    # For demonstration, we'll just print the model name
    print(f"LLM Model Name: {settings.LLM_MODEL_NAME}")

if __name__ == "__main__":
    main()