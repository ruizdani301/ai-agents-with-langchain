from langchain.chat_models import init_chat_model
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

#  crear la funcion que lea la bd y cree u json 
def update_json():
    """solo actualiza el json y vectoriza de nuevo ese json si algun producto es cero para tener datos actualizados"""
    pass

def sale_done():
    "tool to register a sale done"
    #tomara los id que se vendierion y lo pasaran
    #a update_json para actulizar el json
    pass
# se necesitara para enviar las tools
#model_with_tools = model.bind_tools(tools)