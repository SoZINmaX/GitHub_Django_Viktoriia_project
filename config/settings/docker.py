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