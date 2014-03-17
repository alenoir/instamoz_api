from .src.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'instamoz',
        'USER': 'instamoz',
        'PASSWORD': 'Instamoz2014!',
        'HOST': 'localhost',
        'PORT': '',
    }
}