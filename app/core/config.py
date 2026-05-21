from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")

    DATABASE_URL = os.getenv("DATABASE_URL")

    LLM_PROVIDER = os.getenv("LLM_PROVIDER")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    RATE_LIMIT = os.getenv("RATE_LIMIT", "5/minute")


settings = Settings()