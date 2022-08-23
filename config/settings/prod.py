from .base import *

ALLOWED_HOSTS = ['3.39.163.171']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'ls-b9a6b15c7619fb1859ed7abccf36ea2967b9a8ee.c36vvyyhk7pk.ap-northeast-2.rds.amazonaws.com',
        'NAME':'pybodb',
        'USER': 'dbmasteruser',
        'PASSWORD' : 'P9I^=1RTTl^ya]I{*Y[~2u[.tVusgoQe',
        'PORT' : 5432
    }
}
