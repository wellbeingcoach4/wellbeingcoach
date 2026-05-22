from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.data.database import get_db

from app.services.history_manager import HistoryManager

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

@router.get("/{user_id}")
async def get_history(
    user_id: str,
    db: Session = Depends(get_db)
):

    history = HistoryManager.get_history(
        db=db,
        user_id=user_id
    )

    return history