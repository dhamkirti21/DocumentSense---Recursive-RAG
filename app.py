from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os
import pdfplumber

from ingestion import ingest_paper, build_faiss_index, documents, embeddings
from retriever import HybridRetriever
from recursive_engine import RecursiveRAG

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

index = None
retriever = None
engine = None

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


def extract_text(filepath):
    if filepath.endswith(".pdf"):
        text = ""
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    if filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    return ""


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global index, retriever, engine

    # Validate file size
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File exceeds 5MB limit")

    # Validate file type
    if not (file.filename.endswith(".pdf") or file.filename.endswith(".txt")):
        raise HTTPException(status_code=400, detail="Only PDF or TXT allowed")

    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as f:
        f.write(content)

    text = extract_text(filepath)

    if not text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text")

    # Chunking
    chunks = {
        f"section_{i}": text[i:i+2000]
        for i in range(0, len(text), 2000)
    }

    documents.clear()
    embeddings.clear()

    ingest_paper(chunks)
    index = build_faiss_index()
    retriever = HybridRetriever(documents, embeddings, index)
    engine = RecursiveRAG(retriever)

    return {"message": "Indexing completed successfully."}


@app.post("/query")
async def query(data: dict):
    global engine

    if not engine:
        raise HTTPException(status_code=400, detail="Upload document first")

    question = data.get("question")
    answer = engine.run(question)

    return {"answer": answer}