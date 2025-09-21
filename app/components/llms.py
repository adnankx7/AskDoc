from langchain_groq import ChatGroq
from app.config.config import GROQ_API_KEY, GROQ_MODEL_NAME

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm(model_name: str = GROQ_MODEL_NAME, api_key: str = GROQ_API_KEY):

    try:
        logger.info("Loading LLM model from Groq...")

        llm = ChatGroq(
            model=model_name,
            temperature=0.3,
            api_key=api_key
        )

        logger.info("LLM model loaded successfully.")

        return llm

    except Exception as e:
        error_message = CustomException("Failed to load LLM model", e)
        logger.error(str(error_message))
