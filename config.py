from pydantic import AnyHttpUrl, BaseSettings
from typing import Any, Dict, List, Optional, Union


class Settings(BaseSettings):
    NAME: str
    API_ENDPOINT: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    class Config:
        env_file = ".env"


settings = Settings()
