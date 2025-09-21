from langchain_huggingface  import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def get_embedding_model():
    try:
        logger.info("Loading HuggingFace Embeddings model...")
        
        model_name = "all-MiniLM-L6-v2"
        embedding_model = HuggingFaceEmbeddings(model_name=model_name)
        
        logger.info("HuggingFace Embeddings model loaded successfully.")
        return embedding_model
    
    except Exception as e:
        error_message = ConnectionResetError(f"Error loading HuggingFace Embeddings model: {str(e)}")
        raise error_message 
    
        