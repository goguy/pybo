import environ
from .base import *

ALLOWED_HOSTS = ['3.39.163.171']

DEBUG = False

STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('DB_HOST'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD' : env('DB_PASSWORD'),
        'PORT' : 5432
    }
}
