from fabric.api import local, env
import os
import random

def app(app):
    env['app'] = app

def setup():
    if not os.path.exists('settings/local.py'):
        with open('settings/local.py', 'w') as fp:
            secret_key = ''.join([
                random.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
                for i in range(50)
            ])
            fp.write('SECRET_KEY = "%s"\n' % secret_key)

def deploy():
    setup()
    local("./manage.py collectstatic --noinput")
    local("./manage.py syncdb")
    local("./manage.py migrate")

