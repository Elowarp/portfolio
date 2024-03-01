from Portfolio.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}

ALLOWED_HOSTS = ['*']

SECRET_KEY="mykey"