import numpy as np
from rank_bm25 import BM25Okapi
from embeddings import get_embedding
from config import TOP_K

class HybridRetriever:
    def __init__(self, documents, embeddings, index):
        self.documents = documents
        self.embeddings = embeddings
        self.index = index
        self.bm25 = BM25Okapi([doc.split() for doc in documents])

    def retrieve(self, query: str):
        # Dense search
        q_emb = np.array([get_embedding(query)]).astype("float32")
        _, dense_ids = self.index.search(q_emb, TOP_K)

        # Sparse search
        sparse_scores = self.bm25.get_scores(query.split())
        sparse_ids = np.argsort(sparse_scores)[-TOP_K:]

        combined_ids = list(set(dense_ids[0]) | set(sparse_ids))
        return [self.documents[i] for i in combined_ids]