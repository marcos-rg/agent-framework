from agent.core.settings import settings
from agent.core.logger import get_logger
from langchain.chat_models import init_chat_model


logger = get_logger(__name__)

class Agent:
    def __init__(self):
        logger.info(f"Initialized Agent with model: {settings.LLM_MODEL_NAME} from provider: {settings.LLM_MODEL_PROVIDER}")

        self.llm = init_chat_model(
            model_provider=settings.LLM_MODEL_PROVIDER,
            model=settings.LLM_MODEL_NAME,
            api_key=settings.API_KEY.get_secret_value()
        )