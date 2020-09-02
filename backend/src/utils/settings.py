import os

from decouple import config

from src import __version__

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPEN_EXCHANGE_API_KEY = config('OPEN_EXCHANGE_API_KEY')
OPEN_EXCHANGE_HOST = config('OPEN_EXCHANGE_HOST', default="https://openexchangerates.org/api")
REDIS_HOST = config("REDIS_HOST", default="localhost")
REDIS_PORT = config("REDIS_PORT", default=6379)
SERVICE_NAME = "FINANCIAL_MANAGER"
ENVIRONMENT = config('ENVIRONMENT', default="dev")
CACHE_BASE_UID = f"{ENVIRONMENT}-financial-account-manager"
HOST = config('HOST')
PORT = config('PORT')
DEBUG = config('DEBUG')

APM_SETTINGS = {
    'SERVICE_NAME': f"{ENVIRONMENT}-{SERVICE_NAME}",
    'SERVICE_VERSION': __version__,
    'COLLECT_LOCAL_VARIABLES': 'all',
    'ELASTIC_APM_SERVER_URL': config('ELASTIC_APM_SERVER_URL'),
    'ELASTIC_APM_CAPTURE_BODY': 'all',
    'CAPTURE_BODY': 'all'
}

DB_URL = f"mysql+pymysql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@" \
         f"{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"
