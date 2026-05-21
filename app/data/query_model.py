from sqlalchemy import Column, Integer, String, Text
from app.data.database import Base

class WellnessSession(Base):
    __tablename__ = "wellness_sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(String, nullable=False)

    mood = Column(String, nullable=False)

    session_text = Column(Text, nullable=False)