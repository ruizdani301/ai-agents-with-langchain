# 🧠 Análisis de Sentimientos y Resumen con LangChain + Google Gemini

Este proyecto utiliza **LangChain** y **Google Gemini** para procesar texto en español, generando un **resumen automático** y un **análisis de sentimiento estructurado en JSON**.

---

## 🚀 Funcionalidades principales

El programa realiza tres pasos clave:

1. 🧹 **Limpieza del texto**  
   Elimina espacios y saltos de línea innecesarios (`clean_text`).

2. 📝 **Resumen del texto**  
   Usa el modelo **Gemini 2.5 Flash** para generar un resumen breve en español (`text_summary`).

3. 💬 **Análisis de sentimiento**  
   Clasifica el texto como **positivo**, **negativo** o **neutro**, y explica brevemente la razón (`analyze_sentiment`).

Al final, ambos resultados se combinan en un solo objeto con `merge_results()`.

---

## 🧩 Requisitos

- Python **3.10+**  
- Clave de API de **Google AI Studio (Gemini)**  
- Archivo `.env` configurado con tu clave:

```bash
GOOGLE_API_KEY=tu_clave_aqui


Texto: ¡Me encanta este producto! Funciona perfectamente y llegó muy rápido.
Resultado: {
  'resumen': 'El producto funciona perfectamente y llegó rápido.',
  'sentimiento': 'positivo',
  'razon': 'El texto usa expresiones de satisfacción y elogio.'
}
--------------------------------------------------

⚡ Modelo utilizado

Modelo: gemini-2.5-flash

Temperatura: 0 → garantiza resultados consistentes y determinísticos, ideales para tareas analíticas como el análisis de sentimientos.