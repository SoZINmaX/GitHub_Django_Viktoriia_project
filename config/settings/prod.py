from .docker import *
from decouple import config

HOST1=config('HOST1')

DEBUG = False
ALLOWED_HOSTS = [HOST1]