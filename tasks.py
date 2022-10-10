import os
from invoke import task
from decouple import config

@task
def run(ctx):
    print('Creating migrations')
    ctx.run('./manage.py makemigrations')
    print('Migrating db')
    ctx.run('./manage.py migrate')
    print('Collecting static')
    ctx.run('./manage.py collectstatic --noinput')

    cmd = ('uwsgi --http 0.0.0.0:8000 --master '
           '--module "django.core.wsgi:get_wsgi_application()" '
           '--processes 2 '
           '--offload-threads 4 '
           '--enable-threads '
           '--static-map /static=/project/static')
    
    PY_AUTORELOAD = config('PY_AUTORELOAD', default = False)
    
    if PY_AUTORELOAD == True:
          cmd += ' --py-autoreload 1' 
          cmd += ' --harakiri 30'
          
    ctx.run(cmd)