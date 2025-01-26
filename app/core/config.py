from typing import List
from decouple import config
from pydantic import AnyHttpUrl, BaseModel

class Settings(BaseModel):
    API_V1_STR: str = config("API_V1_STR", cast=str)
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM: str = config("JWT_ALGORITHM", cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 5
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000"
    ]
    PROJECT_NAME: str = "Farmer Management"

    #database
    POSTGRES_USER: str = config("POSTGRES_USER", cast=str)
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", cast=str)
    POSTGRES_HOST: str = config("POSTGRES_HOST", cast=str)
    POSTGRES_PORT: int = config("POSTGRES_PORT", cast=int)
    POSTGRES_DATABASE: str = config("POSTGRES_DATABASE", cast=str)
    POSTGRES_ENGINE: str = config("POSTGRES_ENGINE", cast=str)

    class Config:
        case_sensitive = True

settings = Settings()