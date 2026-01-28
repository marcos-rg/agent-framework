import pytest
from unittest.mock import patch, MagicMock
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from agent.core.utils import (
    load_chat_model,
    create_human_message,
    create_system_message,
    create_ai_message,
)


@pytest.mark.unit
class TestLoadChatModel:
    """Tests for the load_chat_model function."""

    @patch("agent.core.utils.init_chat_model")
    def test_load_chat_model_calls_init_chat_model(self, mock_init_chat_model):
        """Verify load_chat_model calls init_chat_model with correct arguments."""
        mock_model = MagicMock()
        mock_init_chat_model.return_value = mock_model

        result = load_chat_model(provider="openai", model="gpt-4")

        mock_init_chat_model.assert_called_once_with("gpt-4", model_provider="openai")
        assert result == mock_model

    @patch("agent.core.utils.init_chat_model")
    def test_load_chat_model_with_different_providers(self, mock_init_chat_model):
        """Verify load_chat_model works with different providers."""
        mock_model = MagicMock()
        mock_init_chat_model.return_value = mock_model

        providers = ["openai", "anthropic", "google-genai"]
        for provider in providers:
            load_chat_model(provider=provider, model="test-model")
            mock_init_chat_model.assert_called_with("test-model", model_provider=provider)


@pytest.mark.unit
class TestCreateHumanMessage:
    """Tests for the create_human_message function."""

    def test_create_human_message_returns_human_message(self):
        """Verify create_human_message returns a HumanMessage instance."""
        message = create_human_message("Hello, world!")
        assert isinstance(message, HumanMessage)

    def test_create_human_message_content(self):
        """Verify create_human_message sets the correct content."""
        content = "Test message content"
        message = create_human_message(content)
        assert message.content == content

    def test_create_human_message_empty_string(self):
        """Verify create_human_message handles empty string."""
        message = create_human_message("")
        assert message.content == ""


@pytest.mark.unit
class TestCreateSystemMessage:
    """Tests for the create_system_message function."""

    def test_create_system_message_returns_system_message(self):
        """Verify create_system_message returns a SystemMessage instance."""
        message = create_system_message("You are a helpful assistant.")
        assert isinstance(message, SystemMessage)

    def test_create_system_message_content(self):
        """Verify create_system_message sets the correct content."""
        content = "System prompt content"
        message = create_system_message(content)
        assert message.content == content

    def test_create_system_message_empty_string(self):
        """Verify create_system_message handles empty string."""
        message = create_system_message("")
        assert message.content == ""


@pytest.mark.unit
class TestCreateAIMessage:
    """Tests for the create_ai_message function."""

    def test_create_ai_message_returns_ai_message(self):
        """Verify create_ai_message returns an AIMessage instance."""
        message = create_ai_message("I am an AI assistant.")
        assert isinstance(message, AIMessage)

    def test_create_ai_message_content(self):
        """Verify create_ai_message sets the correct content."""
        content = "AI response content"
        message = create_ai_message(content)
        assert message.content == content

    def test_create_ai_message_empty_string(self):
        """Verify create_ai_message handles empty string."""
        message = create_ai_message("")
        assert message.content == ""
