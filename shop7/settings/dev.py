import os

from base import *

# SECURITY WARNING: don't run with debug turned on in production!
from shop7.settings.base import BASE_DIR

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1:8000', '127.0.0.1:9000']
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop7',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'STORAGE_ENGINE': 'MYISAM',
        'ATOMIC_REQUESTS': True,
    }
}

# EMAIL_BACKEND = "mailer.backend.DbBackend"
EMAIL_SUBJECT_PREFIX = "[Shop7]"

EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'S4nYNTDs'
EMAIL_HOST_USER     = 'helloshop7'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

OSCAR_FROM_EMAIL = 'Team Shop7 <hello@goshop7.com>'
DEFAULT_FROM_EMAIL = 'Team Shop7 <hello@goshop7.com>'

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-43709275-2'

GOOGLE_ANALYTICS_DOMAIN = 'http://www.goshop7.com/'

GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')