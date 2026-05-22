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
├── .env
├── requirements.txt
├── README.md
├── uv.lock
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │  
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── init_db.py
│   │   └── query_model.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── mood_schema.py
│   │   ├── tip_schema.py
|   |   |── wellness_schema.py
│   │   └── recommendation_schema.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── mood.py
│   │   ├── session.py
│   │   ├── tips.py
│   │   ├── history.py
│   │   ├── recommendation.py
│   │   ├── behavior.py
│   │   └── personalization.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── mood_classifier.py
│   │   ├── mood_manager.py
│   │   ├── session_generator.py
│   │   ├── history_manager.py
│   │   ├── quick_tips.py
│   │   ├── tip_manager.py
│   │   ├── personalization_service.py
│   │   └── validators.py
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── cloud_service.py
│   │   └── local_service.py
│   │
│   ├── behavior/
│   │   ├── __init__.py
│   │   ├── behavioral_memory.py
│   │   ├── analytics_engine.py
│   │   └── pattern_detector.py
│   │
│   ├── recommendation/
│   │   ├── __init__.py
│   │   ├── recommendation_engine.py
│   │   └── user_profile.py
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── middleware.py
│   │   ├── logging_middleware.py
│   │   └── rate_limit.py
│   │
│   ├── exceptions/
│   │   ├── __init__.py
│   │   └── handlers.py
│   │
│   ├── prompts/
│   │   ├── tips_prompt.txt
│   │   ├── session_prompt.txt
│   │   └── personalization_prompt.txt
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   ├── logger.py
│   │   └── time_utils.py
│   │
│   └── tests/
│       ├── __init__.py
│       ├── test_mood.py
│       ├── test_session.py
│       ├── test_tips.py
│       ├── test_behavior.py
│       └── test_personalization.py

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

## Database setup

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
    session_text VARCHAR(1000),
    session_type VARCHAR(50),
    successful BOOLEAN,
    feedback_score INT,
    duration_minutes INT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE mood_analysis (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    user_text VARCHAR(1000) NOT NULL,
    detected_mood VARCHAR(100) NOT NULL,
    confidence FLOAT NOT NULL,
    time_of_day VARCHAR(50),
    stressor VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tip_history (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id VARCHAR(50),
    mood VARCHAR(50),
    category VARCHAR(50),
    provider VARCHAR(50),
    tip VARCHAR(1000),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

# API Endpoints

| Method | Endpoint             | Description                        |
| ------ | -------------------- | ---------------------------------- |
| POST   | `/mood/analyze`      | Analyze user mood                  |
| POST   | `/session/generate`  | Generate 5-minute wellness session |
| GET    | `/tips/quick`        | Get quick wellness tips            |
| GET    | `/history/{user_id}` | Fetch user session history         |
| GET    | `/tips/quick         | Get tips based on mood of the user |

Your app is a genuine AI microservice architecture:

FastAPI
  ↓
Router
  ↓
Service Layer
  ↓
LLM Provider Abstraction
  ↓
Gemini OR Ollama

ollama run llama3.1:8b

You now have enough historical data (MoodAnalysis, WellnessSession, TipHistory) to build a personalized recommendation engine.

## Let’s implement a clean recommendation system that:

Learns from user mood history
Detects repeated emotional patterns
Suggests personalized wellness tips
Recommends sessions dynamically
Uses AI + behavioral history

Mood history
    ↓
Detect dominant emotional pattern
    ↓
Generate recommendation

## Excellent next step. 
## Now you're evolving from a simple AI app into a context-aware behavioral wellness system.

This layer becomes your:

Behavioral Memory Engine

which learns from:

emotional patterns
stress triggers
successful interventions
daily rhythms
Goal

Track:

Behavioral Signal	Purpose
Mood Frequency	Detect emotional trends
Time of Day	Identify vulnerable hours
Repeated Stressors	Understand triggers
Successful Sessions	Learn what helps users


## LLM-Powered Personalization
Now you’re entering the most important layer of your platform:

This transforms your system from:

rule-based wellness app

into:

context-aware AI behavioral coach

The AI will now personalize recommendations using:

mood history
repeated stressors
vulnerable time patterns
successful sessions
behavioral memory

# Target Architecture
User History
    ↓
Behavioral Memory
    ↓
Prompt Builder
    ↓
Gemini / Ollama
    ↓
Personalized AI Recommendation

AI now understands:
WHEN user struggles
WHAT causes stress
WHICH sessions help
HOW to personalize guidance