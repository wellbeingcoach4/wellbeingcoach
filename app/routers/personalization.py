from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.data.database import get_db

from app.services.personalization_service import (
    PersonalizationService
)

router = APIRouter(
    prefix="/personalization",
    tags=["Personalization"]
)


@router.get("/{user_id}")
async def personalized_recommendation(
    user_id: str,
    db: Session = Depends(get_db)
):

    return PersonalizationService.generate_recommendation(
        db=db,
        user_id=user_id
    )