from fastapi import APIRouter
from api.api_v1.handlers import farm

router = APIRouter()

router.include_router(
    farm.farm_router,
    prefix='/farm',
    tags=['farm']
)
