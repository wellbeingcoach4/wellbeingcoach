from pydantic import BaseModel

class WellnessRequest(BaseModel):
    user_id: str
    mood: str


class WellnessResponse(BaseModel):
    session: str