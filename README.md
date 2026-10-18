# PDF Chatbot — RAG-Based Document Question Answering

A PDF question-answering application that allows users to upload a document and ask questions in natural language. The system combines a Flutter mobile interface with a Python backend, document retrieval, vector embeddings, and a large language model to generate context-aware answers.

## Features

- **PDF Upload:** Select a PDF from the device and view its filename and file size before uploading.
- **Document Processing:** Extract text from PDFs and split it into smaller chunks for efficient retrieval.
- **Semantic Embeddings:** Convert document chunks into numerical vector representations.
- **Vector Storage:** Store document embeddings in ChromaDB for similarity-based retrieval.
- **Contextual Retrieval:** Search for relevant passages based on the user's question.
- **AI Question Answering:** Use Google Gemini to generate answers based on the retrieved document context.
- **REST API:** Connect the Flutter frontend to the Python backend using FastAPI endpoints.
- **Mobile Integration:** Provide a Flutter interface for document selection, uploading, and asking questions.
- **Modular RAG Pipeline:** Separate document ingestion, embedding generation, retrieval, and answer generation into distinct stages.

## Architecture

PDF Upload → Text Extraction → Text Chunking → Embeddings → ChromaDB → Similarity Search → Retrieved Context → Gemini → Answer

## Technology Stack

| Technology | Purpose |
|---|---|
| Flutter / Dart | Mobile application interface |
| Python | Backend and RAG processing |
| FastAPI | REST API |
| LangChain | LLM application and RAG integration |
| ChromaDB | Vector storage and retrieval |
| Sentence Transformers | Text embeddings |
| Google Gemini | Context-aware answer generation |
| PDF processing library | PDF text extraction |

The previous development setup used a Sentence Transformers embedding model and a local ChromaDB vector store. Confirm the exact package versions and PDF parser in the current repository before publishing the final technical specifications.

## API Workflow

- `POST /upload` — Submit a PDF for processing and indexing.
- `POST /ask` — Submit a question and receive an AI-generated answer.

The endpoints represent the previously discussed Flutter-backend integration; verify their current request and response schemas in the source code.

## Why This Project?

This project demonstrates practical implementation of Retrieval-Augmented Generation, semantic search, vector databases, prompt-based answer generation, and mobile-to-backend integration. It explores how document retrieval can make language-model applications more useful for answering questions about specific documents.

## Future Improvements

- Display source passages and PDF page references alongside answers.
- Support searching across multiple uploaded documents.
- Add conversation history and persistent document libraries.
- Implement token-by-token streaming responses.
- Support scanned PDFs using OCR.
- Add retrieval evaluation, error handling, and automated tests.

## Important Limitation

Answers may be incomplete or incorrect if the PDF contains insufficient information or the retrieval pipeline selects irrelevant passages. Users should verify important information against the original document.

**Project type:** AI-powered document assistant  
**Core concept:** Retrieval-Augmented Generation (RAG)
