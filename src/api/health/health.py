from fastapi import APIRouter
from pydantic import BaseModel


class HealthResult(BaseModel):
    is_alive: bool

router = APIRouter()

@router.get("/", response_model=HealthResult, name="heartbeat")
def get_health() -> HealthResult:
    health = HealthResult(is_alive=True)
    return health