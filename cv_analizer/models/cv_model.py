from pydantic import BaseModel, Field
from typing import Annotated

class CVAnalysiModel(BaseModel):

    candidate_name: Annotated[str, Field(..., description="Full name of the candidate")]
    years_of_experience: Annotated[int, Field(..., description="Total years of professional experience")]
    skills: Annotated[list[str], Field(..., description="List of key relevant skills possessed by the candidate")]
    education_level: Annotated[str, Field(..., description="Highest level of education attained by the candidate")]
    relevant_experience: Annotated[str, Field(..., description="Description of relevant work experience related to the job applied for")]
    strengsths: Annotated[list[str], Field(..., description="List of candidate's strengths")]
    improvements_areas: Annotated[list[str], Field(..., description="List of 2 - 4 areas where the candidate can improve")]
    overall_fit: Annotated[int, Field(..., description="Overall fit of the candidate in percentaje (0-100) for the job applied for")]
    