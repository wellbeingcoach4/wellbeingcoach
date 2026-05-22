from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.data.database import get_db
from app.models.wellness_session_schema import SessionRequest, SessionResponse
from app.services.history_manager import HistoryManager

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

@router.get("/{user_id}", response_model=list[SessionResponse])
async def get_history(
    user_id: str,
    db: Session = Depends(get_db)
):

    history: list[SessionResponse] = HistoryManager.get_history(
        db=db,
        user_id=user_id
    )

    return history