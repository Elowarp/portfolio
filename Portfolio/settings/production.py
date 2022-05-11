from Portfolio.settings.common import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'HOST': os.getenv("DB_HOST"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'PORT': os.getenv("DB_PORT"),
    }
}

INSTALLED_APPS += (
    'gunicorn',
)

ALLOWED_HOSTS = ['127.0.0.0', 'localhost']

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
