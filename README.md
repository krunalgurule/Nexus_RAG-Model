# RAG Project

This repository demonstrates a Retrieval-Augmented Generation (RAG) system with modular agents and a modern chatbot frontend.

## Overview

- **Backend**: Python-based RAG pipeline with document scraping, storage, retrieval, and evaluation.
- **Frontend**: Next.js chatbot interface for user interaction.
- **Vector Store**: Uses ChromaDB for efficient document retrieval.

## Features

### Backend
- Modular agent architecture (`agent_communication.py`, `document_agent.py`, `scrape_agent.py`)
- Document scraping and ingestion
- Vector storage with ChromaDB (`chroma_store/`)
- RAG pipeline (`rag.py`)
- Evaluation tools (`evaluator.py`, `rag_metrics.json`)
- Requirements listed in `requirements.txt`

### Frontend
- Next.js 16+ app in `chatbot/`
- Chatbot UI for interacting with RAG backend
- TypeScript, Tailwind CSS, and modern React structure

## Getting Started

### Backend Setup
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the RAG pipeline or agents as needed:
   ```sh
   python rag.py
   ```

### Frontend Setup
1. Navigate to the chatbot directory:
   ```sh
   cd chatbot
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```

## Directory Structure

```
rag_project/
├── backend/
│   ├── agent_communication.py
│   ├── document_agent.py
│   ├── evaluator.py
│   ├── rag.py
│   ├── scrape_agent.py
│   ├── requirements.txt
│   └── chroma_store/
│       └── chroma.sqlite3
├── chatbot/
│   ├── src/
│   │   └── app/
│   │       └── chatbot/
│   ├── package.json
│   └── ...
└── README.md
```

## Evaluation & Metrics
- Evaluation scripts and metrics are provided in `backend/evaluator.py` and `rag_metrics.json`.
- Use these to assess retrieval and generation quality.

## Screenshots
- Example screenshots are available in the `screenshots/` directory.

## License
This project is for educational and research purposes.
