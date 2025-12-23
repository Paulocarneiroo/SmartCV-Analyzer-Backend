from pydantic import BaseModel
from typing import List, Optional


class AnalysisResult(BaseModel):
    strengths: List[str]
    weaknesses: List[str]
    compatibility_score: int


class AnalysisResponse(BaseModel):
    id: str
    status: str
    result: Optional[AnalysisResult] = None
