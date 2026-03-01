import faiss
import numpy as np
from embeddings import get_embedding

documents = []
metadata = []
embeddings = []

def ingest_paper(sections: dict):
    for section, text in sections.items():
        chunk = text[:2000]  # minimal chunking
        emb = get_embedding(chunk)

        documents.append(chunk)
        metadata.append({"section": section})
        embeddings.append(emb)

def build_faiss_index():
    dim = len(embeddings[0])
    index = faiss.IndexFlatIP(dim)  # cosine similarity (normalized)
    index.add(np.array(embeddings).astype("float32"))
    return index