from pydantic import BaseModel


class RecommendationResponse(BaseModel):

    user_id: str

    dominant_mood: str

    mood_pattern: str

    recommended_tip: str

    recommended_session: str

    confidence: float