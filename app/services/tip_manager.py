from sqlalchemy.orm import Session

from app.data.query_model import TipHistory


class TipManager:

    @staticmethod
    def save_tip(
        db: Session,
        user_id: str,
        mood: str,
        category: str,
        tip: str,
        provider: str
    ):

        tip_entry = TipHistory(
            user_id=user_id,
            mood=mood,
            category=category,
            tip=tip,
            provider=provider
        )

        db.add(tip_entry)

        db.commit()

        db.refresh(tip_entry)

        return tip_entry