from .base import *

STATICFILES_DIRS = [BASE_DIR / 'static']
ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]