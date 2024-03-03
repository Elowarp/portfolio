from Portfolio.settings.common import *
import os

DEBUG = False

host = "mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority".format(
    os.getenv("DB_USERNAME"),
    os.getenv("DB_PASSWORD"),
    os.getenv("DB_CLUSTER"),
)

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv("DB_NAME"),
        'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': host
            }  
    }
}

INSTALLED_APPS += (
    'gunicorn',
)

ALLOWED_HOSTS = ['127.0.0.0', 'localhost', 'www.elowarp.fr']

MEDIA_ROOT = "/var/www/portfolio/media/"

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
