import os

from .base_settings import *

# Dev Environment specific settings
DEBUG = False 
ALLOWED_HOSTS = ['api.axiologue.org']

#Staticfiles settings
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Development URLs
ROOT_URLCONF = 'axiologue.production_urls'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'watched_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/axiologue.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['watched_file',],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
