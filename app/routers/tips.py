from fastapi import APIRouter

from app.models.schemas import TipResponse

from app.services.quick_tips import QuickTips

router = APIRouter(
    prefix="/tips",
    tags=["Tips"]
)

@router.get("/quick", response_model=TipResponse)
async def get_tip():

    return {
        "tip": QuickTips.get_tip()
    }