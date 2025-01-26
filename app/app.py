from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from database.database import get_db
from api.api_v1.router import router

app = FastAPI(title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    get_db()

app.include_router(
    router, 
    prefix=settings.API_V1_STR
)