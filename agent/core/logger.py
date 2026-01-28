import logging
import sys
from functools import lru_cache


@lru_cache(maxsize=1)
def setup_logger(
    name: str = "agent",
    level: int = logging.INFO,
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """
    Set up and configure the application logger.

    Args:
        name: The name of the logger (default: "agent")
        level: The logging level (default: logging.INFO)
        log_format: The format string for log messages

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding multiple handlers if logger is already configured
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)

        # Formatter
        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Get a logger instance. If a name is provided, it will be a child logger
    of the main 'agent' logger.

    Args:
        name: Optional name for the logger. If provided, creates a child logger.

    Returns:
        logging.Logger: Logger instance
    """
    # Ensure the root logger is set up
    setup_logger()

    if name:
        return logging.getLogger(f"agent.{name}")
    return logging.getLogger("agent")
