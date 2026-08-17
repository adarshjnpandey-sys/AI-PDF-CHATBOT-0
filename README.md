# AI-PDF-CHATBOT
# 🤖 AI PDF Chatbot Using RAG

An AI-powered PDF chatbot that allows users to upload a PDF and ask questions about its content. The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the document and generate context-aware answers using **Google Gemini**.

## 🚀 Features

* 📄 Upload and read PDF documents
* ✂️ Split PDF text into smaller chunks
* 🔎 Semantic similarity search
* 🧠 Google Gemini LLM integration
* 🗄️ Chroma vector database
* 💬 Interactive Streamlit chatbot
* 📝 SQLite-based chat history
* 🤖 Normal AI chat mode
* 🔐 API key management using `.env`

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* LangChain
* ChromaDB
* PyPDF2
* SQLite
* python-dotenv

## 🔄 Working Process

**PDF → Text Extraction → Text Chunking → Embeddings → ChromaDB → Similarity Search → Gemini → Answer**

## 📂 Project Structure

```text
AI-PDF-CHATBOT/
│
├── app.py
├── pdf_utils.py
├── vector_store.py
├── history.py
├── ask_question.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/YOUR-USERNAME/AI-PDF-Chatbot-RAG.git
cd AI-PDF-Chatbot-RAG
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

## 🎯 Purpose

The project demonstrates how **Generative AI, RAG, embeddings, vector databases, and LLMs** can be combined to build an intelligent document question-answering system.

## 🔮 Future Improvements

* Multiple PDF support
* User authentication
* Source/page citations
* Voice-based interaction
* Document summarization
* Cloud deployment

## 👨‍💻 Author

**Adarsh Pandey**
B.Tech Information Technology
JIS College of Engineering
