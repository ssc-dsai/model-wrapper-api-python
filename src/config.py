from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.1"
APP_NAME = "ECD Example"
API_PREFIX = "/api"

config = Config("../.env")

#API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
MODEL_NAME: str = config("MODEL_NAME")
TENANT_ID: str = config("TENANT_ID")
SPN_ID: str = config("SPN_ID")
SPN_PWD: str = config("SPN_PWD")