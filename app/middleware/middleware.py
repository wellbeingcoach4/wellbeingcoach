from fastapi.middleware.cors import CORSMiddleware


CORS_CONFIG = {
    "allow_origins": ["*"],  # change in production (e.g. https://yourdomain.com)
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}