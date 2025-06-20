import os
import json
import re
import time
from register_update import update_json
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent



def sale_done():
    "tool to register a sale done"
    #tomara los id que se vendierion y lo pasaran
    #a update_json para actulizar el json
    pass

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

tools = [search_medicine]
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai", temperature=0)
memory = MemorySaver()
models_with_tools = model.bind_tools([search_medicine])
def agent_chat(request_client):
        messages = [
        SystemMessage("Your are a pharmacist and seller of medicines try to sell medicines to the customers helping with information about medicines be clear, output max 50 characters"),
        HumanMessage(request_client),
    ]

        agent_executor = create_react_agent(model, tools, checkpointer=memory)
    
        config = {"configurable": {"thread_id": "abc123"}}
        for step in agent_executor.stream(
            {"messages": messages}, config, stream_mode="values"
        ):
            step["messages"][-1]
            print(step["messages"][-1])
            return step["messages"][-1]

a = ""
request_client = ""
while request_client != "salir":
    request_client = input("What medicine are you looking for?")
    # configure basic variables
   
    a = agent_chat(request_client)
    
    time.sleep(4)
    print(a)
    # def agent_chat(request_client):
    #     messages = [
    #     SystemMessage("Your are a pharmacist and seller of medicines try to sell medicines to the customers helping with information about medicines be clear, output max 50 characters"),
    #     HumanMessage(request_client),
    # ]

    #     agent_executor = create_react_agent(model, tools, checkpointer=memory)
    
    #     config = {"configurable": {"thread_id": "abc123"}}
    #     for step in agent_executor.stream(
    #         {"messages": messages}, config, stream_mode="values"
    #     ):
    #         step["messages"][-1]
    #         print(step["messages"][-1])

        




    # if __name__ == "__main__":
#question = input("What medicine are you looking for?")
#     update_json()
#     search_medicine()
#agent_chat(question)