from .base import *

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TFT',
        'USER': 'root',
        'PASSWORD': 'wlaks451',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}