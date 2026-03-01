import requests
from config import LLM_URL, LLM_MODEL

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are analyzing a research paper.
Answer strictly using the provided context.
If missing information, say INSUFFICIENT_CONTEXT.

Context:
{context}

Question:
{question}
"""

    try:
        response = requests.post(
            LLM_URL,
            json={
                "model": LLM_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        # Debug safe extraction
        if "response" in data:
            return data["response"]

        if "error" in data:
            raise Exception(f"Ollama error: {data['error']}")

        raise Exception(f"Unexpected Ollama response: {data}")

    except Exception as e:
        return f"LLM ERROR: {str(e)}"