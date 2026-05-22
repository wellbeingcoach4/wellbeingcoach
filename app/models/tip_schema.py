from pydantic import BaseModel

class TipResponse(BaseModel):
    mood: str
    category: str
    tip: str
    provider: str