import os

from src.document_loader import load_pdf
from src.chunker import split_text
from src.embedding import create_embeddings
from src.vector_store import get_collection


def ingest_document(file_path, filename):

    print("Loading PDF...")

    text = load_pdf(file_path)

    if not text.strip():
        print("No text could be extracted from the PDF.")
        return 0

    print(f"PDF loaded. Characters: {len(text)}")


    print("Splitting text into chunks...")

    chunks = split_text(text)

    print(f"Total chunks created: {len(chunks)}")


    print("Creating embeddings...")

    embeddings = create_embeddings(chunks)

    print(f"Total embeddings created: {len(embeddings)}")


    print("Connecting to ChromaDB...")

    collection = get_collection()


    print("Storing chunks in ChromaDB...")

    ids = [
        f"{filename}_chunk_{i}"
        for i in range(len(chunks))
    ]


    metadatas = [
        {
            "source": filename,
            "chunk_number": i
        }
        for i in range(len(chunks))
    ]


    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


    print("\nDocument ingestion completed successfully!")

    print(f"Total chunks stored: {len(chunks)}")

    return len(chunks)