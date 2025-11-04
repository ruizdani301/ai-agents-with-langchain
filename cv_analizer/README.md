# Analizador de cv

Este proyecto consiste en desarrollar una aplicación que reciba como entrada un currículum (CV) y una descripción del puesto de trabajo.
La aplicación, mediante el uso de un modelo de lenguaje (LLM), analizará ambos textos para determinar:

El porcentaje de compatibilidad (match) entre el perfil del candidato y los requisitos del puesto.

Un resumen del perfil del candidato, destacando fortalezas y áreas de mejora.

Las habilidades más relevantes identificadas en el CV.

Esta herramienta está diseñada para apoyar a profesionales de Recursos Humanos (RRHH) en los procesos de selección de personal, facilitando la evaluación y comparación de candidatos de forma rápida y objetiva.

## Ejemplo de interfaz
![alt text](/cv_analizer/img/image.png)

# Arquitectura de carpetas
## models
En este se ubicaran los tipos creados con pydanti
## prompt
En este se ubucaran los promps utilizados para las consultas a los modelos de lenguaje, con los prompts templates
## services
Se crean todos los ficheros que ofreen servicios a la funconalidad principal
## ui
En este se ubucaran los ficheros relacionados con la interfaz de usuario elaborada con streamlilt

herramientas:
- Langchain
- Streamlit
- Pydantic
- Gemini

Nota: Se debe crear una archivo .env en la raiz y agregar GOOGLE_API_KEY="Tu api-key"
ESto en caso que quieran trabajar con un modelo de google.

Author:
- Daniel Ruiz