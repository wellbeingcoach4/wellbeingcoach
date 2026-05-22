from collections import Counter

from sqlalchemy.orm import Session

from app.data.query_model import (
    MoodAnalysis,
    WellnessSession,
    TipHistory
)


class RecommendationEngine:

    @staticmethod
    def generate(
        db: Session,
        user_id: str
    ):

        moods = db.query(
            MoodAnalysis
        ).filter(
            MoodAnalysis.user_id == user_id
        ).all()

        if not moods:

            return {
                "dominant_mood": "neutral",
                "mood_pattern": "insufficient_data",
                "recommended_tip": "Start tracking your moods daily.",
                "recommended_session": "1-minute mindfulness session",
                "confidence": 0.50
            }

        mood_list = [
            mood.detected_mood
            for mood in moods
        ]

        dominant_mood = Counter(
            mood_list
        ).most_common(1)[0][0]

        recommendations = {

            "anxious": {
                "pattern": "frequent_anxiety",
                "tip": "Practice box breathing before stressful situations.",
                "session": "2-minute grounding exercise",
                "confidence": 0.93
            },

            "sad": {
                "pattern": "low_mood_pattern",
                "tip": "Take a short outdoor walk daily.",
                "session": "Positive reflection session",
                "confidence": 0.89
            },

            "stressed": {
                "pattern": "high_stress_pattern",
                "tip": "Pause every hour for deep breathing.",
                "session": "Quick stress reset session",
                "confidence": 0.91
            },

            "neutral": {
                "pattern": "balanced_state",
                "tip": "Maintain hydration and movement.",
                "session": "Daily wellness maintenance",
                "confidence": 0.78
            }
        }

        result = recommendations.get(
            dominant_mood,
            recommendations["neutral"]
        )

        return {
            "user_id": user_id,
            "dominant_mood": dominant_mood,
            "mood_pattern": result["pattern"],
            "recommended_tip": result["tip"],
            "recommended_session": result["session"],
            "confidence": result["confidence"]
        }