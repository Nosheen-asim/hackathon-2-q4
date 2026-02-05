from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database settings
    database_url: str = ""

    # Auth settings
    auth_secret: str = ""
    auth_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Frontend URL for CORS
    frontend_url: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


settings = Settings()