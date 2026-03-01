import os

LLM_URL = os.getenv("LLM_URL", "http://localhost:11434/api/generate")
EMBED_URL = os.getenv("EMBED_URL", "http://localhost:11434/api/embeddings")

LLM_MODEL = "llama3.2:latest"
EMBED_MODEL = "nomic-embed-text:latest"

TOP_K = 2
MAX_RECURSION_DEPTH = 3