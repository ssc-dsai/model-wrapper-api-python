from fastapi import APIRouter
from pydantic import BaseModel


class HearbeatResult(BaseModel):
    is_alive: bool

router = APIRouter()

@router.get("/", response_model=HearbeatResult, name="heartbeat")
def get_hearbeat() -> HearbeatResult:
    heartbeat = HearbeatResult(is_alive=True)
    return heartbeat