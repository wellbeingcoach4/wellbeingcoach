from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.data.database import get_db

from app.models.recommendation_schema import (
    RecommendationResponse
)

from app.recommendation.recommendation_engine import (
    RecommendationEngine
)

router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"]
)


@router.get(
    "/{user_id}",
    response_model=RecommendationResponse
)
async def get_recommendation(
    user_id: str,
    db: Session = Depends(get_db)
):

    return RecommendationEngine.generate(
        db=db,
        user_id=user_id
    )