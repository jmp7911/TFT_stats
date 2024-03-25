from .base import *


ALLOWED_HOSTS = ['*']

# Provider Configurations
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        "APP": {
            "client_id": env("GOOGLE_CLIENT_ID"),
            "secret": env("GOOGLE_SECRET_KEY"),
            "key": ""
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}