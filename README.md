# 🧠 Nexus RAG - Intelligent Document Assistant

![Nexus RAG Landing Page](./screenshots/landing_page.png)

### [🚀 Live Demo: https://nexus-rag-model.vercel.app](https://nexus-rag-model.vercel.app)

**Nexus RAG** is a modern Retrieval-Augmented Generation (RAG) application that allows users to chat with their documents (PDFs) and webpages. Built with a focus on speed, accuracy, and a premium user experience.

---

## ✨ Key Features

-   **📄 Multi-Format Support**: Upload PDFs or provide URL links to chat with web content.
-   **🤖 Advanced RAG Engine**: Uses **Groq (Llama-3)** for lightning-fast inference and **HuggingFace** for efficient embeddings.
-   **📊 Self-Evaluation**: Built-in evaluation agent that checks answers for *Correctness*, *Groundedness*, and *Relevance* in real-time.
-   **⚡ Cloud Native**: Fully deployed on **Render** (Backend) and **Vercel** (Frontend).
-   **🎨 Modern UI**: Beautiful, responsive interface built with Next.js and Tailwind CSS.

![Chat Interface](./screenshots/chat_page.png)

---

## 🛠️ Tech Stack

### Frontend
-   **Framework**: Next.js 15 (App Router)
-   **Styling**: Tailwind CSS
-   **Icons**: Lucide React

### Backend
-   **API**: FastAPI (Python)
-   **LLM**: Groq API (Llama-3-70b-versatile)
-   **Embeddings**: HuggingFace Inference API (all-MiniLM-L6-v2)
-   **Vector DB**: ChromaDB (Persistent)
-   **PDF Processing**: PyPDF2
-   **Web Scraping**: BeautifulSoup4

---

## 🚀 Getting Started (Run Locally)

Follow these steps to run Nexus RAG on your machine.

### Prerequisites
-   Node.js & npm
-   Python 3.10+
-   Git

### 1. Clone the Repository
```bash
git clone https://github.com/krunalgurule/Nexus_RAG-Model.git
cd Nexus_RAG-Model
```

### 2. Backend Setup
```bash
cd backend
# Create virtual environment
python -m venv venv
# Activate it (Windows)
.\venv\Scripts\activate
# Activate it (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
# Add your keys:
# GROQ_API_KEY=your_key_here
# HUGGINGFACEHUB_API_TOKEN=your_token_here

# Run Server
python rag.py
```
*Backend will run on `http://localhost:8000`*

### 3. Frontend Setup
```bash
# Open a new terminal
cd chatbot

# Install dependencies
npm install

# Create .env.local file
# NEXT_PUBLIC_API_URL=http://localhost:8000

# Run Development Server
npm run dev
```
*Frontend will run on `http://localhost:3000`*

---

## 🔒 Environment Variables

| Variable | Description |
| :--- | :--- |
| `GROQ_API_KEY` | API Key from [Groq Console](https://console.groq.com/) |
| `HUGGINGFACEHUB_API_TOKEN` | Read Token from [HuggingFace](https://huggingface.co/settings/tokens) |
| `NEXT_PUBLIC_API_URL` | Cloud Backend URL (for Vercel) or localhost (for dev) |

---

## 📄 License
MIT License. Free to use and modify for personal and commercial projects.

---
*Built with ❤️ by Krunal Gurule.*
