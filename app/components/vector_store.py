import os
from langchain_community.vectorstores import FAISS

from app.components.embeddings import get_embedding_model

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing FAISS vector store...")
            return FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
        
        else:
            logger.warning(f"FAISS vector store not found ..")
            
    except Exception as e:
        error_message = CustomException("Failed to load FAISS vector store", e)
        logger.error(str(error_message))
        
### Creating new vector store
def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No text chunks available to create vector store")
        
        logger.info("Creating new FAISS vector store...")
        
        embedding_model = get_embedding_model()
        
        db = FAISS.from_documents(text_chunks, embedding_model)
        
        logger.info(f"Saving FAISS vector store...")
        
        db.save_local(DB_FAISS_PATH)    
        
        logger.info("FAISS vector store saved successfully")
        
        return db
    
    except Exception as e:
        error_message = CustomException("Failed to Create new FAISS vector store", e)
        logger.error(str(error_message))