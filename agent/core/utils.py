from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage

def create_human_message(message: str) -> HumanMessage:
    return HumanMessage(content=message)

def create_system_message(message: str) -> SystemMessage:
    return SystemMessage(content=message)

def create_ai_message(message: str) -> AIMessage:
    return AIMessage(content=message)