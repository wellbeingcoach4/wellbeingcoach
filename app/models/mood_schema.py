from pydantic import BaseModel
from typing import Optional


class MoodRequest(BaseModel):
    mood: str
    message: str
    provider: Optional[str] = "gemini"


class MoodResponse(BaseModel):
    mood: str
    recommendation: str