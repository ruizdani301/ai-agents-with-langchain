import os
import json
import re
from all_tools.all_tools import search_medicine
from register_update import update_json
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

tools = [search_medicine]
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai", temperature=0)
memory = MemorySaver()
models_with_tools = model.bind_tools([search_medicine])



def sale_done():
    "tool to register a sale done"
    #tomara los id que se vendierion y lo pasaran
    #a update_json para actulizar el json
    pass


def agent_chat(request_client):
        template = ChatPromptTemplate([
        ("system", "Your are a pharmacist and seller of medicines try to sell medicines to the customers helping with information about medicines be clear, output max 50 characters"),
        ("human", f"{request_client}"),
    ])

        template_message = template.format(request_client=request_client)

        agent_executor = create_react_agent(model, tools, checkpointer=memory)
    
        config = {"configurable": {"thread_id": "abc123"}}
        for step in agent_executor.stream(
            {"messages": template_message}, config, stream_mode="values"
        ):
            step["messages"][-1]
           # print(step["messages"][-1])
        return step["messages"][-1]

a = ""
request_client = ""
while request_client != "salir":
    request_client = input("What medicine are you looking for?")
    # configure basic variables
    a = agent_chat(request_client)
    print(a.content)





    # if __name__ == "__main__":
#question = input("What medicine are you looking for?")
#     update_json()
#     search_medicine()
#agent_chat(question)