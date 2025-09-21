from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from app.components.llms import load_llm
from app.components.vector_store import load_vector_store

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import GROQ_API_KEY, GROQ_MODEL_NAME

logger = get_logger(__name__)

CUSTOM_PROMPT = """
You are a knowledgeable AI medical assistant designed to help users with their health and medical questions. Your goal is to provide helpful, accurate information based on the available context and general medical knowledge.

INSTRUCTIONS:
1. Always try to provide a helpful response using the context provided
2. If the context contains relevant medical information, use it to give a comprehensive answer
3. If the context is limited, supplement with general medical knowledge when appropriate
4. Only say "I don't know" if the question is completely unrelated to medicine or health
5. Be informative, clear, and reassuring in your responses
6. Structure answers to be easily understandable
7. Focus on providing actionable, practical information

CONTEXT INFORMATION:
{context}

USER QUESTION: {question}

MEDICAL ASSISTANT RESPONSE:
"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT, input_variables=["context", "question"])

def create_qa_chain():
    try:
        logger.info("Loading vector store for context")

        db = load_vector_store()

        if db  is None:
            raise CustomException("Vector store not present or empty")

        llm = load_llm(model_name=GROQ_MODEL_NAME, api_key=GROQ_API_KEY)

        if llm  is None:
            raise CustomException("LLM not loaded")

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 1}),  # Increased from 1 to 3 for better context
            return_source_documents=False ,
            chain_type_kwargs={"prompt": set_custom_prompt()}
        )

        logger.info("QA chain created successfully")
        return qa_chain
    except Exception as e:
        error_message = CustomException("Error in creating QA chain", e)
        logger.error(str(error_message))
