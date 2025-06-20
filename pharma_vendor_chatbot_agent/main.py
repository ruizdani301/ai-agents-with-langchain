import os
from all_tools.all_tools import search_medicine, sale_done
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

tools = [search_medicine, sale_done]
model = init_chat_model("gemini-2.0-flash",
                        model_provider="google_genai",
                        temperature=0)
memory = MemorySaver()

os.environ["GOOGLE_API_KEY"] = "your-Google-api-key"

def main_agent():

    def agent_chat(request_client):
        template = ChatPromptTemplate([
                                        ("system", "You are a pharmacist and medicine seller. Try to sell medicines to the customer. ""When closing the sale, ask for the customer's name and address. Then return a JSON like this: ""{{\"name\": \"<name>\", \"address\": \"<address>\", \"id\": <medicine_id>, \"quantity\": <quantity>}} ""Respond naturally. Limit normal messages to 50 characters."),
                                        ("human", f"{request_client}"),
                                    ])
        template_message = template.format(request_client=request_client)
        agent_executor = create_react_agent(model, tools,
                                            checkpointer=memory)
        config = {"configurable": {"thread_id": "abc123"}}
        for step in agent_executor.stream(
            {"messages": template_message}, config, stream_mode="values"
        ):
            step["messages"][-1]
        return step["messages"][-1]

    a = ""
    request_client = ""
    while request_client != "salir":
        request_client = input("What medicine are you looking for?")
        a = agent_chat(request_client)
        print(a.content)


if __name__ == "__main__":
    main_agent()
