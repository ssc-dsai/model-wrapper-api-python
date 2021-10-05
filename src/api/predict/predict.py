from fastapi import APIRouter, Body

from starlette.requests import Request

router = APIRouter()

@router.post("/")
def post_predict(request: Request, records: dict = Body(...)):
    model = request.app.state.model
    result = model.run(records)
    return result