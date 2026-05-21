from pydantic import BaseModel

class MoodRequest(BaseModel):
    user_id: str
    text: str


class MoodResponse(BaseModel):
    mood: str
    confidence: float