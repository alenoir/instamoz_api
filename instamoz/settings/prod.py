from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'instamoz',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'antoinelenoir',
        'PASSWORD': 'antoinelenoir',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

if environ.has_key('DATABASE_URL'):
    url = urlparse(environ['DATABASE_URL'])
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }

INSTAGRAM_CONFIG = {
    'client_id': '7ba882f721c4412cadb351f29ba8109f',
    'client_secret': '0d475653225f4b2188337a721d4e3a5d',
    'redirect_uri': 'http://http://calm-sands-6994.herokuapp.com/realtime-instagram/'
}