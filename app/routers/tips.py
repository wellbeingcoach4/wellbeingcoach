from fastapi import APIRouter, Query

from app.models.schemas import TipResponse

from app.services.quick_tips import QuickTips

router = APIRouter(
    prefix="/tips",
    tags=["Tips"]
)

@router.get("/quick", response_model=TipResponse)
async def get_quick_tip(mood: str = Query(
        default="neutral",
        description="User emotional state"
    )):
    
    result = QuickTips.get_tip(mood)

    return {
        "mood": mood,
        **result
    }