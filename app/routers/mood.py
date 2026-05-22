from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.mood_schema import (
    MoodRequest,
    MoodResponse
)

from app.services.mood_classifier import MoodClassifier
from app.services.mood_manager import MoodManager

from app.data.database import get_db

router = APIRouter(
    prefix="/mood",
    tags=["Mood"]
)


@router.post(
    "/classify",
    response_model=MoodResponse
)
async def analyze_mood(
    payload: MoodRequest,
    db: Session = Depends(get_db)):

    result = MoodClassifier.analyze(payload.text)

    MoodManager.save_mood(
        db=db,
        user_id=payload.user_id,
        user_text=payload.text,
        detected_mood=result["mood"],
        confidence=result["confidence"]
    )

    return result