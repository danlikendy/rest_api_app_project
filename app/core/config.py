import os
from typing import Optional

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./organizations.db")
    API_KEY: str = os.getenv("API_KEY", "your-secret-api-key-here")
    
    class Config:
        env_file = ".env"

settings = Settings()
