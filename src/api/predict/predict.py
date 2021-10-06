from fastapi import APIRouter, Body, Depends
from starlette.requests import Request

from helpers.security import validate_request

router = APIRouter()

@router.post("/")
def post_predict(request: Request, records: dict = Body(...)):
    model = request.app.state.model
    result = model.run(records)
    return result

# Example with API key
# @router.post("/")
# def post_predict(request: Request, authenticated: bool = Depends(validate_request), records: dict = Body(...)):
#     model = request.app.state.model
#     result = model.run(records)
#     return result