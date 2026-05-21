"""Database connection and operations for storing LLM query records."""

from __future__ import annotations

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.query_model import Base, LLMQuery

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env file!")

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# Ensure the required table exists before inserting records.
Base.metadata.create_all(bind=engine)


def save_llm_query(user_query: str, llm_response: str) -> LLMQuery:
    """Save a user query and model response to PostgreSQL."""
    with SessionLocal() as session:
        record = LLMQuery(user_query=user_query, llm_response=llm_response)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
