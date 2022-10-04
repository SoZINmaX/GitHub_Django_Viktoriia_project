from .settings import *
from decouple import config

# DATABASE STUFF

NAME=config('POSTGRES_DB')
USER=config('POSTGRES_USER')
PASSWORD=config('POSTGRES_PASSWORD')
HOST=config('POSTGRES_HOST')
PORT=config('POSTGRES_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
        'ATOMIC_REQUESTS': True
    }
}

# volumes 

MEDIA_URL = '/media/'
MEDIA_ROOT = '/project/media/'

STATIC_URL = '/static/'
STATIC_ROOT = '/project/static/'

# celery

CELERY_BROKER_URL = config('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')