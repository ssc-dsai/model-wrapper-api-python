from copy import Error
from fastapi import FastAPI

from config import (API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG) 
from model import Model
from routes import api_router


app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)

#Loading API Routes
app.include_router(api_router, prefix=API_PREFIX)

#Loading Model
active_model = Model()
active_model.init()

if(active_model.model):
    app.state.model = active_model
else:
    raise Error('Could not initiate model')

@app.get("/")
def read_root():
    return {"version": APP_VERSION}