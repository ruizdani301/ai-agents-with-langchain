from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                            temperature=0,
                            google_api_key=GOOGLE_API_KEY
                            )

def clean_text(text: str) -> str:
    """Cleans the input text by removing extra
       whitespace and newlines.
    """
    return (' '.join(text.split()))[:500]


def text_summary(text:str):
    """Creates a Runnable that processes text using
       the Google Gemini model and cleans the output.
    """
    prompt = f"Summarize the following text in spanish:\n\n{text}\n\nSummary:"
    llm_response = llm.invoke(prompt)
    return llm_response.content


def analyze_sentiment(text:str):
    """Analiza el sentimiento y devuelve resultado estructurado"""

    prompt = f"""Analiza el sentimiento del siguiente texto {text}.
    Responde ÚNICAMENTE en formato JSON válido sin usar comillas triples ni ningún otro
    tipo de delimitador. El JSON debe tener la siguiente estructura:
    {
        {"sentimiento": "positivo|negativo|neutro",
         "razon": "justificación breve"
         }
     }
    """
    response = llm.invoke(prompt)
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        print("Error al decodificar JSON")
        return {"error": "Respuesta no es un JSON válido",
                "respuesta": response.content}
    
def merge_results(data:dict):
    """combine the results to deliver a single object"""
    return {
        "resumen": data["summary"],
        "sentimiento": data["sentiment_data"]["sentimiento"],
        "razon": data["sentiment_data"]["razon"]
    }

def initial_process(text: str):
    """integrates two functions."""
    summary:str = text_summary(text)
    sentiment_obj = analyze_sentiment(summary)

    return merge_results({
        "summary": summary,
        "sentiment_data": sentiment_obj
    })

initial = RunnableLambda(initial_process)
chain_one = RunnableLambda(clean_text)

final_chain = chain_one | initial

# Prueba con diferentes textos
textos_prueba = [
    "¡Me encanta este producto! Funciona perfectamente y llegó muy rápido.",
    "El servicio al cliente fue terrible, nadie me ayudó con mi problema.",
    "El clima está nublado hoy, probablemente llueva más tarde."
]
 
for texto in textos_prueba:
    resultado = final_chain.invoke(texto)
    print(f"Texto: {texto}")
    print(f"Resultado: {resultado}")
    print("-" * 50)
