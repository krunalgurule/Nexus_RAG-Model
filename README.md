# Nexus RAG

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15+-000000.svg?logo=next.js&logoColor=white)
![Groq](https://img.shields.io/badge/AI-Groq-f55036.svg?logo=google-cardboard&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg?logo=fastapi&logoColor=white)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-orange)

### **Fast. Cloud-Ready. Powerful.**
**Nexus RAG** is a modular Retrieval-Augmented Generation system designed for cloud deployment. It leverages the **Groq API** for lightning-fast inference (Llama 3 70B) and **HuggingFace Embeddings** for CPU-efficient vector search.

[Features](#key-features) • [Tech Stack](#tech-stack) • [Installation](#installation) • [Usage](#usage)

</div>

---

## 🚀 Key Features

*   **⚡ Blazing Fast AI**: Powered by **Groq API**, utilizing Llama 3 70B for near-instant responses.
*   **☁️ Cloud Ready**: Optimized for deployment (Render, Railway, Vercel) by removing heavy local dependencies (Ollama).
*   **📄 Document Ingestion**: Upload PDF documents to create a searchable knowledge base.
*   **🌐 Web Scraping**: Ingest and analyze content directly from URLs.
*   **🧠 Vector Search**: Uses **ChromaDB** and **HuggingFace Embeddings** (CPU-friendly) for semantic search.
*   **🤖 Modular Agents**: Architecture built with specialized agents for scraping, document processing, and evaluation.
*   **📊 RAG Evaluation**: Built-in metrics to assess answer correctness, relevance, and groundedness.

## 🛠️ Tech Stack

### Backend
*   **Python 3.10+** (FastAPI)
*   **LangChain** (Framework)
*   **ChromaDB** (Vector Store)
*   **Groq API** (LLM - Llama 3 70B)
*   **HuggingFace** (Embeddings)
*   **PyMuPDF** (PDF Processing)
*   **Trafilatura** (Web Scraping)

### Frontend
*   **Next.js 15+** (React Framework)
*   **TypeScript**
*   **Tailwind CSS**
*   **Lucide React** (Icons)

---

## 📦 Installation

### Prerequisites
1.  **Python**: 3.10 or higher.
2.  **Node.js**: v18 or higher.
3.  **Groq API Key**: Get one for free at [console.groq.com](https://console.groq.com/).

### 1. Backend Setup
Navigate to the backend directory and set up the environment:

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate  # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

**Create a `.env` file** in the `backend` folder and add your key:
```env
GROQ_API_KEY=gsk_your_key_here
```

### 2. Frontend Setup
Open a new terminal, navigate to the chatbot directory, and install dependencies:
```powershell
cd chatbot
npm install
```

---

## ⚡ Usage

### Start the Application

**Terminal 1 (Backend):**
```powershell
cd backend
python rag.py
```
*Server runs on `http://0.0.0.0:8000`*

**Terminal 2 (Frontend):**
```powershell
cd chatbot
npm run dev
```
*UI runs on `http://localhost:3000`*

### How to Use
1.  Open **[http://localhost:3000](http://localhost:3000)** in your browser.
2.  **Upload a PDF** using the attachment icon or **Paste a URL** to ingest content.
3.  Ask questions! The AI will answer based on the context of your uploaded documents.

---

## 📂 Project Structure

```
nexus-rag/
├── backend/                # Python FastAPI Backend
│   ├── rag.py              # Main Server Entry Point
│   ├── document_agent.py   # PDF Processing Logic
│   ├── scrape_agent.py     # URL Scraping Logic
│   ├── evaluator.py        # RAG Evaluation Metrics (Groq Powered)
│   └── chroma_store/       # Vector Database (Local)
├── chatbot/                # Next.js Frontend
│   ├── src/app/            # App Router & Pages
│   └── package.json        # Frontend Dependencies
└── README.md               # Project Documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
