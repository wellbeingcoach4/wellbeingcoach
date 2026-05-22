from fastapi import APIRouter, Query
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.schemas import TipResponse

from app.routers import mood
from app.services.quick_tips import QuickTips

from app.services.tip_manager import TipManager

from app.data.database import get_db

from app.core.config import settings

router = APIRouter(
    prefix="/tips",
    tags=["Tips"]
)

@router.get("/quick", response_model=TipResponse)
async def get_quick_tip(
    mood: str = Query(default="neutral", description="User emotional state"),
    user_id: str = Query(default="u101", description="User ID"),
    db: Session = Depends(get_db)
):
    
    result = QuickTips.get_tip(mood)

    TipManager.save_tip(
        db=db,
        user_id=user_id,
        mood=mood,
        category=result["category"],
        tip=result["tip"],
        provider=settings.LLM_PROVIDER
    )

    return {
        "mood": mood,
        "user_id": user_id,
        "category": result["category"],
        "tip": result["tip"],
        "provider": settings.LLM_PROVIDER
    }