import requests
from config import EMBED_URL, EMBED_MODEL

def get_embedding(text: str):
    response = requests.post(
        EMBED_URL,
        json={
            "model": EMBED_MODEL,
            "prompt": text
        }
    )

    if response.status_code != 200:
        raise Exception(f"Embedding failed: {response.text}")

    return response.json()["embedding"]