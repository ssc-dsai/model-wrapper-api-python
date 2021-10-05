from fastapi import APIRouter

from config import (APP_VERSION) 
from api.heartbeat import heartbeat
from api.predict import predict

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["heartbeat"], prefix="/heartbeat")
api_router.include_router(predict.router, tags=["predict"], prefix="/predict")

@api_router.get("/")
def read_root():
    return {"version": APP_VERSION}