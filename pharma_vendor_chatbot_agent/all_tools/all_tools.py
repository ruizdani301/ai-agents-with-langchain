import json
import os
from langchain_core.tools import tool
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from conection import get_conection

os.environ["GOOGLE_API_KEY"] = "your-Google-api-key"
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
    vectorizer_embeddings = GoogleGenerativeAIEmbeddings(
                                                        model="models/embedding-001", task_type="SEMANTIC_SIMILARITY"
                                                        )
    vector_store = InMemoryVectorStore.from_texts(data, vectorizer_embeddings)
    docs = vector_store.similarity_search(text_request, k=1)
    for document in docs:
        return document.page_content


@tool
def sale_done(name: str, address: str, id: int, quantity: int):
    """
        tool to register a sale done required client
        name, id of the medicine and quantity
    """
    try:
        conn = get_conection()
        cursor = conn.cursor()
        cursor.execute("UPDATE medicament SET cantidad = cantidad - ? WHERE id = ? AND cantidad >= ?", (quantity, id, quantity))
        conn.commit()
    except Exception as e:
        print(f"Error updating quantity: {e}")
        return "Error updating quantity in the database."
    finally:
        conn.close()
    return f"The medicine name, will be delivered to {name}, to the address: {address}, the quantity of {quantity}"
