import os
import shutil

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from src.rag import ask_question,preview_document
from src.ingest import ingest_document,get_collection


app = FastAPI()
class PreviewRequest(BaseModel):

    filename: str

class QuestionRequest(BaseModel):
    question: str
    filename: str


@app.get("/")
def home():

    return {
        "message": "RAG Chatbot API is running!"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):

        return {
            "error": "Only PDF files are allowed."
        }


    os.makedirs("documents", exist_ok=True)

    file_path = os.path.join(
        "documents",
        file.filename
    )


    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    chunks_stored = ingest_document(
        file_path,
        file.filename
    )


    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "chunks_stored": chunks_stored
    }

@app.post("/ask")
def ask(request: QuestionRequest):

    answer = ask_question(
        request.question,
        request.filename
    )

    return {
        "question": request.question,
        "filename": request.filename,
        "answer": answer
    }

@app.get("/documents")
def get_documents():

    collection = get_collection()

    results = collection.get(
        include=["metadatas"]
    )

    documents = {}

    for metadata in results["metadatas"]:

        filename = metadata["source"]

        if filename not in documents:

            documents[filename] = 0

        documents[filename] += 1

    document_list = []

    for filename, chunks in documents.items():

        document_list.append({
            "filename": filename,
            "chunks": chunks
        })

    return {
        "documents": document_list
    }

@app.post("/preview")
def preview(request: PreviewRequest):

    preview = preview_document(
        request.filename
    )

    return {
        "filename": request.filename,
        "preview": preview
    }