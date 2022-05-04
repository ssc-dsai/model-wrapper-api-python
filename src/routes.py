from fastapi import APIRouter

from config import (APP_VERSION) 
from api.health import health
from api.predict import predict

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"], prefix="/health")
api_router.include_router(predict.router, tags=["predict"], prefix="/predict")

@api_router.get("/")
def read_root():
    return {"version": APP_VERSION}