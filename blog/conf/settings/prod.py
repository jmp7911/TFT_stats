from .base import *

ALLOWED_HOSTS = ['54.180.146.14']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://54.180.146.14",
    "http://54.180.146.14:8000",
    "http://localhost",
]