from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Google Gemini with LangChain", page_icon="🤖")
st.title("Google Gemini with LangChain 🤖")
st.markdown("""
This is a simple demo of using Google Gemini Pro model with LangChain.
""")
#definimmos el sidebar para configurar el modelo y la temperatura
with st.sidebar:
    st.header("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.5-pro"])

# Inicializamos el modelo de chat de Google Generative AI
chat_model = ChatGoogleGenerativeAI(model=model_name,
                              temperature=temperature,
                              google_api_key=GOOGLE_API_KEY
                              )
# Inicializar el estado de la sesion para almacenar los mensajes
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant.")
    ]


template = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that helps people find information."),
            ("human", "{historial}\nrespond to: {mensaje}")
        ])
# Crear la cadena de prompts
cadena = template | chat_model

#Boton de eliminar conversacion, borra el estado
st.button("Clear Conversation", on_click=lambda: st.session_state.messages.clear())


for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        continue
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):    
        st.markdown(msg.content)

# cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu pregunta aqui...")
if pregunta:
    with st.chat_message("user"):
        st.markdown(pregunta)
    try:
    
        with st.chat_message("assistant"):
                response_placeholder = st.empty()
                full_response = ""  
                for chunk in cadena.stream({ "mensaje" : pregunta, "historial": st.session_state.messages}):
                    full_response += chunk.content
                    print(full_response)
                    response_placeholder.markdown(full_response + "▌")  # Muestra la respuesta con un cursor    
                response_placeholder.markdown(full_response)  # Finaliza la respuesta sin el cursor
        #st.markdown(respuesta.content)
        st.session_state.messages.append(HumanMessage(content=pregunta))
        st.session_state.messages.append(AIMessage(content=full_response))
    except Exception as e:
        st.error(f"Error: {e}")
