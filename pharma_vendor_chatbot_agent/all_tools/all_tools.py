import json
import os
from langchain_core.tools import tool
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


@tool
def search_medicine(text_request):
    """
    Search for a medicine requested.

    Args:
        text_request (str): The name of the medicine to search for.

    Returns:
        str: The description of the document containing the medicine found.
    """
    with open('medicaments.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    vectorizer_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", task_type="SEMANTIC_SIMILARITY")
    vector_store = InMemoryVectorStore.from_texts(data, vectorizer_embeddings)
    docs = vector_store.similarity_search(text_request, k=1)
    for document in docs:
        return document.page_content