from sqlalchemy.orm import Session

from app.data.query_model import (
    MoodAnalysis,
    WellnessSession,
    TipHistory
)

from app.llm.cloud_service import GeminiService
from app.llm.local_service import OllamaService

from app.core.config import settings

from collections import Counter


class PersonalizationService:

    @staticmethod
    def generate_recommendation(
        db: Session,
        user_id: str
    ):

        # -------------------------
        # Fetch behavioral history
        # -------------------------

        moods = db.query(
            MoodAnalysis
        ).filter(
            MoodAnalysis.user_id == user_id
        ).all()

        sessions = db.query(
            WellnessSession
        ).filter(
            WellnessSession.user_id == user_id
        ).all()

        tips = db.query(
            TipHistory
        ).filter(
            TipHistory.user_id == user_id
        ).all()

        # -------------------------
        # Build analytics
        # -------------------------

        mood_frequency = Counter(
            [m.detected_mood for m in moods]
        )

        dominant_mood = (
            mood_frequency.most_common(1)[0][0]
            if moods else "neutral"
        )

        stressors = Counter(
            [m.stressor for m in moods]
        )

        top_stressor = (
            stressors.most_common(1)[0][0]
            if moods else "unknown"
        )

        successful_sessions = [
            s.session_text
            for s in sessions
            if s.successful
        ]

        # -------------------------
        # Build AI prompt
        # -------------------------

        prompt = f"""
        You are an empathetic AI wellbeing coach.

        User behavioral profile:

        Dominant mood:
        {dominant_mood}

        Frequent stressor:
        {top_stressor}

        Successful wellness sessions:
        {successful_sessions[:3]}

        Generate:
        1. One personalized wellness recommendation
        2. One short actionable tip
        3. One motivational sentence

        Keep response supportive and concise.
        """

        # -------------------------
        # Select provider
        # -------------------------

        provider = settings.LLM_PROVIDER.lower()

        if provider == "gemini":

            llm = GeminiService()

            ai_response = llm.generate(prompt)

        else:

            llm = OllamaService()

            ai_response = llm.generate(prompt)

        return {
            "user_id": user_id,
            "dominant_mood": dominant_mood,
            "top_stressor": top_stressor,
            "recommendation": ai_response
        }