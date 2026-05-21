# wellbeingcoach

Wellbeing Coach is an AI-powered web application that delivers a personalized 5-minute mental wellness session to users whenever they need a quick reset. Think of it as a pocket-sized mental health companion that listens to how you are feeling, understands your context, and responds with a short, actionable plan to help you feel better.

Built using FastAPI and PostgreSQL, the application focuses on scalable APIs, secure validation, rate limiting, exception handling, and AI-driven personalized coaching experiences.

| Component          | Technology              |
| ------------------ | ----------------------- |
| Backend Framework  | FastAPI                 |
| Language           | Python                  |
| LLM Provider       | Google Gemini OR Ollama |
| Validation         | Pydantic                |
| Database           | PostgreSQL              |
| ORM                | SQLAlchemy              |
| Rate Limiting      | slowapi                 |
| API Docs           | Swagger/OpenAPI         |
| Environment Config | python-dotenv           |
| Server             | Uvicorn                 |
| Testing            | Pytest                  |

# project structure

WELLBEINGCOACH

WELLBEINGCOACH/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── constants.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── query_model.py
│   │
│   ├── exceptions/
│   │   └── handlers.py
│   │
│   ├── llm/
│   │   ├── cloud_service.py
│   │   └── local_service.py
│   │
│   ├── middleware/
│   │   └── rate_limit.py
│   │
│   ├── models/
│   │   ├── mood_schema.py
│   │   └── schemas.py
│   │
│   ├── routers/
│   │   ├── history.py
│   │   ├── mood.py
│   │   ├── session.py
│   │   └── tips.py
│   │
│   ├── services/
│   │   ├── history_manager.py
│   │   ├── mood_classifier.py
│   │   ├── quick_tips.py
│   │   ├── session_generator.py
│   │   └── validators.py
│   │
│   └── tests/
│       └── test_routes.py
│
├── requirements.txt
├── .env
└── README.md

# FastAPI Starter Architecture

Features Included
FastAPI application setup
Environment configuration with python-dotenv
PostgreSQL + SQLAlchemy setup
Pydantic request/response validation
Rate limiting with slowapi
Modular clean architecture
Exception handling
AI provider abstraction (Gemini/Ollama)
4 basic API endpoints

# API Endpoints

| Method | Endpoint             | Description                        |
| ------ | -------------------- | ---------------------------------- |
| POST   | `/mood/analyze`      | Analyze user mood                  |
| POST   | `/session/generate`  | Generate 5-minute wellness session |
| GET    | `/tips/quick`        | Get quick wellness tips            |
| GET    | `/history/{user_id}` | Fetch user session history         |

Start PostgreSQL
psql postgres

\du for roles
\l to list database
\dt to list tables

CREATE DATABASE wellbeing
\l

\c wellbeing

CREATE TABLE wellness_sessions (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id VARCHAR(50),
    mood VARCHAR(100),
    session_text VARCHAR(1000)
);