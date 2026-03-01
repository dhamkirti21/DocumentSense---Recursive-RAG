from config import MAX_RECURSION_DEPTH
from llm import generate_answer

class RecursiveRAG:
    def __init__(self, retriever):
        self.retriever = retriever

    def detect_gap(self, answer: str):
        return "INSUFFICIENT_CONTEXT" in answer

    def run(self, question: str, depth=0):
        if depth > MAX_RECURSION_DEPTH:
            return "Unable to answer with available evidence."

        chunks = self.retriever.retrieve(question)
        context = "\n\n".join(chunks)

        answer = generate_answer(context, question)

        if self.detect_gap(answer):
            refined_q = question + " provide more technical explanation"
            return self.run(refined_q, depth + 1)

        return answer