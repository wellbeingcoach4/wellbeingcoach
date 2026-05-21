from fastapi import FastAPI

from app.core.config import settings

from app.middleware.rate_limit import limiter

from fastapi.middleware.cors import CORSMiddleware
from app.middleware.middleware import CORS_CONFIG

from app.exceptions.handlers import (
    generic_exception_handler
)

from app.routers import (
    mood,
    session,
    tips,
    history
)

from app.data.database import Base, engine
from app.data.query_model import (
    MoodAnalysis,
    WellnessSession
)

app = FastAPI(
    title=settings.APP_NAME
)

Base.metadata.create_all(bind=engine)

app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    **CORS_CONFIG
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(mood.router)

app.include_router(session.router)

app.include_router(tips.router)

app.include_router(history.router)


@app.get("/")
async def root():

    return {
        "message": "Wellbeing Coach API Running"
    }