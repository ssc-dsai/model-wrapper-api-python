from fastapi import APIRouter, Body, Depends
from starlette.requests import Request

from helpers.messages import INACTIVE_MODEL
from helpers.security import validate_request

router = APIRouter()

@router.post("/")
def post_predict(request: Request, records: dict = Body(...)):

    #Load model
    model = request.app.state.model

    if(model):
        result = model.run(records)
    else:
        raise Exception(INACTIVE_MODEL)

    return result

# Example with API key
# @router.post("/")
# def post_predict(request: Request, authenticated: bool = Depends(validate_request), records: dict = Body(...)):
    # #Load model
    # model = request.app.state.model

    # if(model):
    #     result = model.run(records)
    # else:
    #     raise Exception(INACTIVE_MODEL)
        
    # return result