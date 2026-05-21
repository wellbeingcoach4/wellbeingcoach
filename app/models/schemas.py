from pydantic import BaseModel

class SessionRequest(BaseModel):
    user_id: str
    mood: str


class SessionResponse(BaseModel):
    session: str


class TipResponse(BaseModel):
    tip: str