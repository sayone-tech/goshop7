from base import *

# SECURITY WARNING: don't run with debug turned on in production!
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

EMAIL_BACKEND = "mailer.backend.DbBackend"
EMAIL_SUBJECT_PREFIX = "[Shop7]"

EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'developer@sayone'
EMAIL_HOST_USER     = 'developer.sayone@gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
