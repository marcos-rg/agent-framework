from agent.main import Agent

from agent.core.logger import get_logger
logger = get_logger(__name__)

def main():
    agent = Agent()
    logger.info("Agent initialized successfully.")
    

if __name__ == "__main__":
    main()