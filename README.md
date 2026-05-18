# AI Support Governance System

Production-style AI orchestration system built using LangChain, LangGraph, FAISS, Flask, and OpenAI-compatible LLM workflows.

The system simulates how modern AI support platforms handle customer requests through retrieval-augmented generation (RAG), confidence-based routing, escalation handling, and conversational memory.

Instead of directly generating responses for every query, the workflow retrieves relevant company policy context, evaluates confidence, and decides whether the request should be answered automatically or escalated for human review.

---

# Architecture

```text
User Query
    ↓
Retriever
    ↓
Confidence Scoring
    ↓
Router
 ┌───────────────┴───────────────┐
 │                               │
ALLOW                        ESCALATE
 │                               │
LLM Response             Human Review
```

---

# Features

- LangGraph workflow orchestration
- Retrieval-Augmented Generation (RAG)
- FAISS vector similarity search
- Confidence-based routing
- Escalation handling
- Session-based memory
- Flask API interface

---

# Tech Stack

- Python
- LangChain
- LangGraph
- FAISS
- Flask
- HuggingFace Embeddings
- OpenAI-compatible LLM workflows

---

# Project Structure

```text
lang_chain_project/
│
├── app.py
├── chains/
├── graphs/
├── rag/
├── memory/
├── utils/
├── data/
├── faiss_index/
└── screenshots/
```

---

# Setup

## Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Build Vector Index

```bash
python rag/build_index.py
```

---

## Run Application

```bash
python app.py
```

---

# API Testing

## Standard Query

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:5000/chat" `
-Method POST `
-ContentType "application/json" `
-Body '{"question":"Can I get a refund after 20 days?"}'
```

---

## Escalation Query

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:5000/chat" `
-Method POST `
-ContentType "application/json" `
-Body '{"question":"I will file a legal complaint regarding GDPR violation"}'
```

---

# Example Response

```json
{
  "confidence": 0.86,
  "decision": "ALLOW",
  "response": "Customers are eligible for refunds within 30 days of purchase."
}
```

---

# Screenshots

- FAISS index creation
- Flask server execution
- Successful response generation

---

# Future Improvements

- PostgreSQL-backed memory
- Redis caching
- Docker deployment
- Streaming responses
- Production observability
- Multi-agent workflows

---

# Author

Tajwinder Singh