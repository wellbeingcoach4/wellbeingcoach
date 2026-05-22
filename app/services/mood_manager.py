from sqlalchemy.orm import Session

from app.behavior.behavioral_memory import BehavioralMemory
from app.data.query_model import MoodAnalysis


class MoodManager:

    @staticmethod
    def save_mood(
        db: Session,
        user_id: str,
        user_text: str,
        detected_mood: str,
        confidence: float
    ):

        mood_entry = MoodAnalysis(
            user_id=user_id,
            user_text=user_text,
            detected_mood=detected_mood,
            confidence=confidence,
            time_of_day=BehavioralMemory.detect_time_of_day(),
            stressor=BehavioralMemory.detect_stressor(
                user_text
            )
        )
        

        db.add(mood_entry)

        db.commit()

        db.refresh(mood_entry)

        return mood_entry