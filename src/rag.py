import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from  src.embedding import create_embedding
from src.vector_store import get_collection


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_question(question, filename):

    # Convert question into a vector
    query_embedding = create_embedding(question)

    # Get ChromaDB collection
    collection = get_collection()

    # Retrieve chunks ONLY from the selected document
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        where={
            "source": filename
        }
    )

    # Get documents from search results
    documents = results["documents"][0]

    # Safety check
    if not documents:
        return "I don't know based on the provided document."

    # Join retrieved chunks into context
    context = "\n\n".join(documents)

    # Create prompt
    prompt = f"""
You are a helpful document assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say exactly:

"I don't know based on the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    # Send prompt to Gemini
    response = llm.invoke(prompt)

    content = response.content

    if isinstance(content, list):

        answer = ""

        for item in content:

            if (
                isinstance(item, dict)
                and item.get("type") == "text"
            ):
                answer += item.get("text", "")

        return answer

    return str(content)
def preview_document(filename):

    collection = get_collection()

    # Get chunks only from the selected document
    results = collection.get(
        where={
            "source": filename
        },
        include=["documents"]
    )

    documents = results["documents"]

    if not documents:
        return "No content was found for this document."

    # Join only this document's chunks
    context = "\n\n".join(documents)

    prompt = f"""
You are an AI document assistant.

Analyze the following document and provide:

1. A short title for the document
2. A brief summary in 3-5 sentences
3. The main topics covered

Keep the response clear and concise.

Document:
{context}
"""

    response = llm.invoke(prompt)

    content = response.content

    if isinstance(content, list):

        answer = ""

        for item in content:

            if (
                isinstance(item, dict)
                and item.get("type") == "text"
            ):
                answer += item.get("text", "")

        return answer

    return str(content)


def start_chat():

    print("RAG Chatbot Started!")
    print("Type 'exit' to stop.\n")


    while True:

        question = input("You: ")


        if question.lower() == "exit":
            print("Chatbot stopped.")
            break


        answer = ask_question(question)


        print(f"\nBot: {answer}\n")


if __name__ == "__main__":
    start_chat()