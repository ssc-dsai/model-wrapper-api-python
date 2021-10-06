from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import (API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG, ALLOWED_ORIGINS)
from helpers.messages import NO_VALID_MODEL 
from model import Model
from routes import api_router


app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Loading API Routes
app.include_router(api_router, prefix=API_PREFIX)

#Loading Model
active_model = Model()
active_model.init()

if(active_model.model):
    app.state.model = active_model
else:
    raise Exception(NO_VALID_MODEL)

@app.get("/")
def read_root():
    return {"version": APP_VERSION}