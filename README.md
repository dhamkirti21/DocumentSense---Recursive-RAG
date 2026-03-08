## 🚀 DoucmentSense - Recursive RAG Architecture
Production-Grade Multi-Hop Retrieval-Augmented Generation System
A high-performance Recursive Retrieval-Augmented Generation (RAG) system engineered for multi-hop reasoning, improved factual grounding, and scalable deployment.

Built with:
FastAPI – High-performance API layer
Local Ollama LLM – On-device inference
FAISS Vector Store – Efficient semantic retrieval
Recursive Query Refinement – Multi-step reasoning
Dockerized Deployment – Clean environment isolation

# 📌 Problem Statement
Traditional RAG systems suffer from:
❌ Incomplete retrieval for multi-hop questions
❌ Context fragmentation across documents
❌ Over-reliance on first-pass retrieval
❌ Hallucination when key facts are missing
This system solves these limitations using recursive retrieval loops with LLM-driven query reformulation.

# 🧠 Core Innovation: Recursive Retrieval Loop
Instead of performing a single retrieval step, this system:
Retrieves initial context
Uses LLM to identify missing knowledge
Generates refined sub-queries
Retrieves additional supporting evidence
Aggregates context
Produces grounded final synthesis
This enables:
Multi-hop reasoning
Dynamic context expansion
Reduced hallucination
Improved answer completeness

# 🏗 System Architecture & Data Flow

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d2c9346f-e4cf-4bb1-82f3-7d41c31a51ee" />

# Architectural Highlights
Clear separation of concerns:
Retrieval layer
Reasoning layer
Aggregation layer
Recursion depth control
Configurable similarity thresholds
Host-container networking architecture
Extensible pipeline design

# 🔁 Detailed Recursive Flow
Step 1 – Initial Retrieval
Query embedding generation
Top-K similarity search via FAISS
Step 2 – Intermediate Reasoning
LLM identifies gaps in retrieved context
Generates structured follow-up queries
Step 3 – Recursive Retrieval
Additional semantic search
Score-based filtering
Context deduplication
Step 4 – Final Synthesis
Aggregated context passed to LLM
Grounded response generation
Source attribution

# 📂 Project Structure
recursive-rag/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── rag_pipeline.py      # Recursive orchestration logic
│   ├── embeddings.py        # Embedding interface
│   ├── retriever.py         # FAISS search abstraction
│   ├── llm_client.py        # Ollama API client
│   └── utils.py
│
├── data/
│   └── documents/
│
├── docker-compose.yml
├── Dockerfile
└── README.md
Designed for modularity and production scalability.

# ⚙️ Technology Stack
Layer	Technology
API	FastAPI
LLM	Ollama (mistral)
Embeddings	nomic-embed-text
Vector DB	FAISS
Deployment	Docker
Runtime	Python 3.10+

# 🔌 Configuration
Since Ollama runs locally (not inside Docker):
Docker Mode
- LLM_URL=http://host.docker.internal:11434/api/generate
- EMBED_URL=http://host.docker.internal:11434/api/embeddings
- Local Development Mode
- LLM_URL=http://localhost:11434/api/generate
- EMBED_URL=http://localhost:11434/api/embeddings

▶️ Running the System
1️⃣ Install Ollama
brew install ollama or winget install ollama 

Pull required models:
ollama pull lamma3.2:latest
ollama pull nomic-embed-text


2️⃣ Local Run (Without Docker)
pip install -r requirements.txt
uvicorn app.main:app --reload


3️⃣ Docker Run (Ollama on Host)
ollama serve
docker-compose up --build
Ensure:
No Ollama service defined in docker-compose.yml
Host networking configured correctly

# 📌 API Contract
POST /query
Request
{
  "query": "Explain vector databases in detail"
}
Response
{
  "answer": "...",
  "sources": [...]
}

# 📊 Engineering Design Decisions
Concern	Solution
Multi-hop reasoning	Recursive query refinement
Hallucination mitigation	Evidence aggregation
Context overflow	Controlled chunk merging
Retrieval precision	Top-K + score filtering
Scalability	Modular pipeline
Deployment flexibility	Host-based LLM + containerized API

# 📈 Production-Ready Enhancements (Roadmap)
Streaming token responses
Hybrid retrieval (BM25 + Dense search)
Redis caching layer
Async LLM calls
Observability (Prometheus + Grafana)
RAG evaluation framework (RAGAS)
Vector persistence & sharding

# 🧪 Real-World Use Cases
Technical documentation QA
Enterprise knowledge base assistant
Research automation
Legal / compliance multi-document reasoning
Internal developer copilots

# 🧩 Key Concepts Demonstrated
Recursive retrieval loops
Multi-hop semantic reasoning
Prompt chaining
Embedding-based similarity search
Context window optimization
LLM grounding strategies
System-level architecture design
Host-container networking

# 🎯 Why This Project Stands Out
Moves beyond toy RAG examples
Demonstrates applied system design
Shows understanding of LLM limitations
Implements practical mitigation strategies
Production-conscious architecture
This is not a wrapper around an LLM — it is a reasoning-aware retriev
