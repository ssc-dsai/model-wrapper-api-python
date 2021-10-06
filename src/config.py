from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.1"
APP_NAME = "API Example"
API_PREFIX = "/api"

ALLOWED_ORIGINS = ['*']

config = Config("../.env")

#API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
MODEL_NAME: str = config("MODEL_NAME")