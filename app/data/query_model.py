"""SQLAlchemy model definitions for LLM query persistence."""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class LLMQuery(Base):
    """Represents a saved query/response pair for the AI tutor."""

    __tablename__ = "llm_queries_tbl"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_query = Column(String(length=1024), nullable=False)
    llm_response = Column(Text, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    def __repr__(self) -> str:
        return (
            f"<LLMQuery(id={self.id}, user_query={self.user_query!r}, "
            f"created_at={self.created_at})>"
        )