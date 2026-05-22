from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from app.data.database import get_db

from app.models.wellness_schema import (
    WellnessRequest,
    WellnessResponse
)

from app.services.session_generator import SessionGenerator
from app.services.history_manager import HistoryManager

router = APIRouter(
    prefix="/session",
    tags=["Session"]
)

@router.post("/generate", response_model=WellnessResponse)
async def generate_session(
    payload: WellnessRequest,
    db: Session = Depends(get_db)
):

    session_text = SessionGenerator.generate(payload.mood)

    HistoryManager.save_session(
        db=db,
        user_id=payload.user_id,
        mood=payload.mood,
        session_text=session_text
    )

    return {
        "session": session_text
    }