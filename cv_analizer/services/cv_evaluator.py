from langchain_google_genai import ChatGoogleGenerativeAI
from models.cv_model import CVAnalysiModel
from prompts.cv_prompts import create_system_prompts
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def create_cv_evaluator_llm():
    """ Create a Google Generative AI LLM for CV evaluation """
    llm_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                            temperature=0,
                            google_api_key=GOOGLE_API_KEY
                            )
    # Enable structured output with CV analysis model
    output_structure = llm_model.with_structured_output(CVAnalysiModel)
    chat_prompt = create_system_prompts()
    evaluation_chain = chat_prompt | output_structure

    return evaluation_chain

def get_cv_evaluator(cv_text: str, job_description: str) -> CVAnalysiModel:
    """ Evaluate the CV text against the job description """
    try:
        llm_chain = create_cv_evaluator_llm()
        evaluation = llm_chain.invoke({
            "text_cv":cv_text,
            "job_description":job_description
        })
        return evaluation
    except Exception as e:
        return CVAnalysiModel(
            candidate_name="N/A",
            years_of_experience=0,
            skills=["No es posible procesar el CV"],
            education_level="N/A",
            relevant_experience="N/A",
            strengsths=["No es posible procesar el CV"],
            improvements_areas=["N/A"],
            overall_fit=0
    )   