from .base import *

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME':'pybodb',
        'USER': 'postgres',
        'PASSWORD' : '12345',
        'PORT' : 5432
    }
}


