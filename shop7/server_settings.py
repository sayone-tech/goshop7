from settings import *

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
ALLOWED_HOSTS = ['goshop7.com','75.126.24.85','www.goshop7.com']

ADMINS = (
     ('Shebin', 'shebinoutlook@gmail.com'),
)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'store',
        'USER': 'sayonestore',
        'PASSWORD': 'pwd@store',
        'HOST': 'localhost',
        'PORT': '',
        'STORAGE_ENGINE': 'MYISAM',
        'ATOMIC_REQUESTS': True,
    }
}

#EMAIL_BACKEND = "mailer.backend.DbBackend"
#EMAIL_SUBJECT_PREFIX = "[Shop7]"

TIME_ZONE = 'Asia/Kolkata'

#EMAIL_HOST          = 'smtp.gmail.com'
#EMAIL_HOST_PASSWORD = 'noreplaydeveloper@sayone'
#EMAIL_HOST_USER     = 'noreplaydeveloper@gmail.com'
#EMAIL_PORT          = 587
#EMAIL_USE_TLS       = True





