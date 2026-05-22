from sqlalchemy.orm import Session

from app.data.query_model import WellnessSession

class HistoryManager:

    @staticmethod
    def save_session(
        db: Session,
        user_id: str,
        mood: str,
        session_text: str
    ):

        record = WellnessSession(
            user_id=user_id,
            mood=mood,
            session_text=session_text
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return record

    @staticmethod
    def get_history(db: Session, user_id: str):

        history = db.query(WellnessSession).filter(
            WellnessSession.user_id == user_id
        ).all()

        return history