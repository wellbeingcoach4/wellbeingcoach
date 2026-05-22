from sqlalchemy import Boolean, Column, Integer, String, Text, Float, DateTime, func
from app.data.database import Base

class WellnessSession(Base):
    __tablename__ = "wellness_sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(String, nullable=False)

    mood = Column(String, nullable=False)

    session_text = Column(Text, nullable=False)

    session_type = Column(String)

    successful = Column(Boolean, default=False)

    feedback_score = Column(Integer)

    duration_minutes = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

class MoodAnalysis(Base):
    __tablename__ = "mood_analysis"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(String, nullable=False)

    user_text = Column(Text, nullable=False)

    detected_mood = Column(String, nullable=False)

    confidence = Column(Float, nullable=False)

    stressor = Column(String)

    time_of_day = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

class TipHistory(Base):

    __tablename__ = "tip_history"

    id = Column(Integer, primary_key=True)

    user_id = Column(String)

    mood = Column(String)

    category = Column(String)

    tip = Column(Text)

    provider = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )