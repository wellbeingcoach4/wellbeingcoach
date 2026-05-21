from fastapi import APIRouter

from app.models.mood_schema import (
    MoodRequest,
    MoodResponse
)

from app.services.mood_classifier import MoodClassifier

router = APIRouter(
    prefix="/mood",
    tags=["Mood"]
)

@router.post("/analyze", response_model=MoodResponse)
async def analyze_mood(payload: MoodRequest):

    result = MoodClassifier.analyze(payload.text)

    return result