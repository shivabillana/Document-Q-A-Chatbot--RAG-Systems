# 📄 Document Q&A Chatbot — RAG System

An AI-powered multi-user document question-answering system built using Retrieval-Augmented Generation (RAG).  
Users can upload documents and interact with them through a chat interface to get context-aware answers.

---

## 🚀 Features

### 📂 Multi-Format Document Support
- Upload multiple files per session
- Supported formats:
  - PDF
  - DOCX
  - TXT
  - HTML

---

### 🧠 Retrieval-Augmented Generation (RAG)
- Context-aware responses using vector similarity search
- Pipeline:
  - Document loading → Chunking → Embedding → Retrieval → LLM

---

### 🔍 Semantic Search
- Embeddings generated using Sentence Transformers
- Efficient retrieval with ChromaDB

---

### 💬 Chat Interface
- Interactive Q&A over uploaded documents
- Multi-turn conversation support
- Context-aware responses

---

### 🧩 Session-Based Architecture
- Each user gets a **unique session**
- Separate ChromaDB collection per session
- No data sharing between users

---

### 🧹 Automatic Cleanup
- Collections auto-delete after inactivity
- Prevents memory leaks and data persistence
- Ensures complete data isolation

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Framework:** LangChain  
- **Vector Database:** ChromaDB  
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)  
- **LLM:** OpenRouter  
- **Document Parsing:** LangChain Loaders  

---

## 📂 Project Structure

├── app.py
├── documentloader.py
├── chunking.py
├── embedding.py
├── vectorstorage.py
├── retrieval.py
├── llm_engine.py
├── .env
├── requirements.txt

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/document-qa-rag.git
cd document-qa-rag
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment

Create `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
MODEL_NAME=your_model_name

CHROMA_DB_API_KEY=your_key
CHROMA_DB_TENANT=your_tenant
CHROMA_DB_DATABASE=your_database
```

---

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 💡 Usage

1. Upload one or more documents
2. Ask questions in chat
3. System retrieves relevant context
4. LLM generates accurate answers

---

## 🔥 Key Highlights

* Multi-user isolation using session-based vector collections
* Automatic cleanup for memory and security
* Full RAG pipeline implementation
* Supports multiple document formats
* Scalable architecture design

---

## 🧠 Core Concepts Used

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Chunking Strategies
* Session Lifecycle Management

---

## 🚀 Future Improvements

* 🔗 Source citation highlighting
* 🧠 Conversation memory
* 📊 Document insights dashboard
* ⚡ Streaming responses
* ☁️ Deployment (AWS / Docker)

---

## 📜 License

MIT License

---

## 👤 Author

Shiva
