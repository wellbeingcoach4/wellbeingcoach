from collections import Counter

from sqlalchemy.orm import Session

from app.data.query_model import MoodAnalysis


class AnalyticsEngine:

    @staticmethod
    def analyze_user_patterns(
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
                "message": "No behavioral data"
            }

        mood_frequency = Counter(
            [m.detected_mood for m in moods]
        )

        stressor_frequency = Counter(
            [m.stressor for m in moods]
        )

        time_patterns = Counter(
            [m.time_of_day for m in moods]
        )

        return {

            "dominant_mood":
                mood_frequency.most_common(1)[0][0],

            "top_stressor":
                stressor_frequency.most_common(1)[0][0],

            "vulnerable_time":
                time_patterns.most_common(1)[0][0],

            "mood_frequency":
                dict(mood_frequency)
        }