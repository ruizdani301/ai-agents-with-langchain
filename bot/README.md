# 🤖 Google Gemini + LangChain + Streamlit Chat App

Este proyecto es una **aplicación de chat interactiva** que utiliza el modelo **Google Gemini** integrado con **LangChain**, y una interfaz en **Streamlit**.  
Permite conversar con un asistente inteligente que responde usando la API de **Google Generative AI**.

---

## 🚀 Características

✅ Interfaz de chat creada con **Streamlit**  
✅ Integración con **Google Gemini (Generative AI)**  
✅ Gestión del historial de conversación con **LangChain Messages**  
✅ Configuración dinámica de **modelo** y **temperatura**  
✅ Respuestas **en tiempo real** (streaming de tokens)  
✅ Botón para **reiniciar la conversación**

---

## 📦 Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener:

- Python **3.10+**
- Una **API Key de Google Generative AI**
- Una cuenta activa en **Google AI Studio** o **Google Cloud**
- Entorno virtual (recomendado)

---

## ⚙️ Instalación

1. **Clona el repositorio o copia los archivos**

   ```bash
   git clone https://github.com/tuusuario/gemini-langchain-chat.git
   cd gemini-langchain-chat

python3 -m venv venv
source venv/bin/activate   # En Linux / Mac
venv\Scripts\activate      # En Windows

pip install streamlit python-dotenv langchain langchain-google-genai


GOOGLE_API_KEY=tu_clave_aqui
```
📁 gemini-langchain-chat
│
├── app.py              # Código principal de la aplicación
├── .env                # Clave de API de Google
├── requirements.txt     # (Opcional) dependencias del proyecto
└── README.md
```
streamlit run app.py
```
chat_model = ChatGoogleGenerativeAI(
    model=model_name,
    temperature=temperature,
    google_api_key=GOOGLE_API_KEY
)

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that helps people find information."),
    ("human", "{historial}\nrespond to: {mensaje}")
])

cadena = template | chat_model

for chunk in cadena.stream({"mensaje": pregunta, "historial": st.session_state.messages}):
    response_placeholder.markdown(full_response + "▌")

```
| Elemento                       | Función                                              |
| ------------------------------ | ---------------------------------------------------- |
| **Sidebar**                    | Permite elegir modelo (`gemini-2.5-*`) y temperatura |
| **Chat Input**                 | Caja de texto para enviar preguntas                  |
| **Botón “Clear Conversation”** | Limpia el historial de mensajes                      |
| **Chat Area**                  | Muestra las interacciones con el asistente           |

```
🧑‍💻 Autor

Tu Nombre
💼 Desarrollador Backend / IA
🌐 LinkedIn
 | GitHub```
