from pydantic import BaseModel, ConfigDict


class SessionRequest(BaseModel):
    user_id: str
    mood: str


class SessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)     
    user_id: str
    mood: str
    session_text: str