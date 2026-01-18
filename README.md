# Nexus RAG

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15+-000000.svg?logo=next.js&logoColor=white)
![Ollama](https://img.shields.io/badge/AI-Ollama-000000.svg?logo=ollama&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg?logo=fastapi&logoColor=white)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-orange)

### **Local. Private. Powerful.**
**Nexus RAG** is a privacy-focused, modular Retrieval-Augmented Generation system. It connects your local documents and web content with powerful AI models running entirely on your machine.

[Features](#key-features) • [Tech Stack](#tech-stack) • [Installation](#installation) • [Usage](#usage)

</div>

---

## 🚀 Key Features

*   **🔒 Privacy-First AI**: Powered by **Ollama**, running open-source models (Llama 3) locally. No data leaves your machine.
*   **📄 Document Ingestion**: Upload PDF documents to create a searchable knowledge base.
*   **🌐 Web Scraping**: Ingest and analyze content directly from URLs.
*   **🧠 Vector Search**: Uses **ChromaDB** and **MxBai Embeddings** for semantic search and retrieval.
*   **🤖 Modular Agents**: Architecture built with specialized agents for scraping, document processing, and evaluation.
*   **📊 RAG Evaluation**: Built-in metrics to assess answer correctness, relevance, and groundedness.

## 🛠️ Tech Stack

### Backend
*   **Python 3.10+** (FastAPI)
*   **LangChain** (Framework)
*   **ChromaDB** (Vector Store)
*   **Ollama** (LLM & Embeddings)
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
1.  **Ollama**: [Download and Install Ollama](https://ollama.com).
2.  **Python**: 3.10 or higher.
3.  **Node.js**: v18 or higher.

### 1. Setup AI Models
Open a terminal and pull the required models:
```powershell
ollama pull llama3
ollama pull mxbai-embed-large
```

### 2. Backend Setup
Navigate to the backend directory and install dependencies:
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```
*Note: Depending on your setup, you might need to use `python3` instead of `python`.*

### 3. Frontend Setup
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
│   ├── evaluator.py        # RAG Evaluation Metrics
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
