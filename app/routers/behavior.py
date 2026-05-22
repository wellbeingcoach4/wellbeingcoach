from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.data.database import get_db

from app.behavior.analytics_engine import (
    AnalyticsEngine
)

router = APIRouter(
    prefix="/behavior",
    tags=["Behavior"]
)


@router.get("/{user_id}")
async def behavioral_insights(
    user_id: str,
    db: Session = Depends(get_db)
):

    return AnalyticsEngine.analyze_user_patterns(
        db=db,
        user_id=user_id
    )