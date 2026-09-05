import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_embedding_model():
    """
    Creates and returns the Gemini embedding model.
    """

    api_key = os.getenv("GOOGLE_API_KEY")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )

    return embeddings