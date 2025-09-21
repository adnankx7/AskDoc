# 🩺 Medical RAG Chatbot

A sophisticated Retrieval-Augmented Generation (RAG) chatbot designed specifically for medical queries and health-related information. This application combines the power of large language models with medical knowledge retrieval to provide accurate, context-aware responses to health questions.

## 🌟 Features

- **Intelligent Medical Assistant**: Powered by Groq's Llama-3.1-8b-instant model with specialized medical prompting
- **Document-Based Knowledge**: Retrieves information from "The GALE ENCYCLOPEDIA of MEDICINE" for accurate medical insights
- **Modern Web Interface**: Clean, responsive chat interface with real-time messaging
- **Session Management**: Maintains chat history during user sessions
- **Error Handling**: Robust error handling with user-friendly error messages
- **Logging System**: Comprehensive logging for debugging and monitoring
- **Vector Search**: FAISS-powered vector store for efficient document retrieval

## 🏗️ Architecture

### Core Components

```
app/
├── application.py          # Main Flask application
├── components/
│   ├── llms.py            # Language model integration (Groq)
│   ├── retriever.py       # RAG chain and prompt management
│   ├── data_loader.py     # PDF processing pipeline
│   ├── pdf_loader.py      # PDF document loading
│   ├── embeddings.py      # Text embedding generation
│   ├── vector_store.py    # FAISS vector store management
│   └── __init__.py
├── config/
│   └── config.py          # Configuration settings
├── templates/
│   └── index.html         # Web interface
└── common/
    ├── logger.py          # Logging utilities
    └── custom_exception.py # Custom exception handling
```

### Technology Stack

- **Backend**: Python 3.8+, Flask
- **AI/ML**: LangChain, Groq API, HuggingFace Transformers
- **Vector Database**: FAISS
- **Document Processing**: PyPDF
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Environment**: python-dotenv

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key
- HuggingFace token (for embeddings)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd medical-rag-chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**

   Create a `.env` file in the root directory:
   ```env
   # Groq API Configuration
   GROQ_API_KEY=your_groq_api_key_here

   # HuggingFace Configuration
   HF_TOKEN=your_huggingface_token_here
   ```

5. **Process Medical Documents**

   The application uses "The GALE ENCYCLOPEDIA of MEDICINE" as its knowledge base. To process and index the documents:

   ```bash
   cd app/components
   python data_loader.py
   ```

   This will:
   - Load the PDF document from `data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf`
   - Split text into chunks (500 tokens with 50 token overlap)
   - Generate embeddings using HuggingFace models
   - Create and save FAISS vector store to `vectorstore/db_faiss/`

## 🏃‍♂️ Running the Application

1. **Start the Flask server**
   ```bash
   python app/application.py
   ```

2. **Access the application**
   Open your browser and navigate to: `http://localhost:5000`

3. **Start chatting**
   - Type your medical questions in the chat interface
   - The AI will retrieve relevant information from the medical encyclopedia
   - Get context-aware, medically-informed responses

## 📖 Usage

### Chat Interface

- **Ask Questions**: Type any medical or health-related question
- **Clear Chat**: Use the clear button (✕) in the header to reset the conversation
- **Session Persistence**: Chat history is maintained during the session

### Example Queries

```
"What are the symptoms of diabetes?"
"How does the cardiovascular system work?"
"What treatments are available for hypertension?"
"Explain the digestive process."
```

## ⚙️ Configuration

### Model Settings

Edit `app/config/config.py` to customize:

```python
# Groq Configuration
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_MODEL_NAME = "llama-3.1-8b-instant"  # Alternative: "mixtral-8x7b-32768"

# Vector Store Settings
DB_FAISS_PATH = "vectorstore/db_faiss"
DATA_PATH = "data/"

# Text Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
```

### Custom Prompts

The medical assistant uses a specialized prompt template defined in `app/components/retriever.py`:

- Provides helpful, accurate medical information
- Uses context from the medical encyclopedia
- Supplements with general medical knowledge when appropriate
- Maintains clear, reassuring communication style

## 🔧 Development

### Project Structure

```
├── app/                    # Main application package
├── data/                   # Medical documents (PDFs)
├── vectorstore/           # FAISS vector database
├── logs/                  # Application logs
├── requirements.txt       # Python dependencies
├── setup.py              # Package configuration
└── README.md             # This file
```

### Adding New Components

1. **New LLM Integration**: Add to `app/components/llms.py`
2. **Custom Retrievers**: Extend `app/components/retriever.py`
3. **Document Loaders**: Add to `app/components/data_loader.py`
4. **Vector Stores**: Modify `app/components/vector_store.py`

### Logging

The application includes comprehensive logging:

- **Info Level**: General application flow
- **Error Level**: Exceptions and failures
- **Debug Level**: Detailed debugging information

Logs are saved to `logs/` directory with timestamps.

## 🧪 Testing

### Manual Testing

1. **Start the application**
2. **Test basic queries**:
   - Simple medical questions
   - Complex health inquiries
   - Edge cases and error scenarios

3. **Verify responses**:
   - Accuracy of medical information
   - Relevance to the query
   - Clarity of explanations

### Automated Testing

```bash
# Run unit tests (if implemented)
python -m pytest tests/

# Load testing for chat interface
# Use tools like Apache JMeter or Locust
```

## 🚨 Important Notes

### Medical Disclaimer

⚠️ **This is an AI-powered tool for informational purposes only.**

- **Not a substitute for professional medical advice**
- **Always consult healthcare professionals** for medical concerns
- **In emergencies, contact emergency services immediately**

### API Limits

- **Groq API**: Monitor usage and rate limits
- **HuggingFace**: Ensure valid token and sufficient quota
- **Vector Store**: FAISS index performance depends on available RAM

### Data Privacy

- Chat sessions are stored in Flask sessions (temporary)
- No persistent storage of user conversations
- Medical documents are processed locally

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with detailed description

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure medical accuracy in any health-related changes

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Groq** for providing fast LLM inference
- **LangChain** for RAG framework
- **HuggingFace** for embedding models
- **FAISS** for efficient vector similarity search
- **The GALE ENCYCLOPEDIA of MEDICINE** for medical knowledge base

## 📞 Support

For issues, questions, or contributions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Include error logs and reproduction steps

---

**Built with ❤️ for healthcare accessibility and education**

*Remember: This tool is designed to supplement, not replace, professional medical advice.*
