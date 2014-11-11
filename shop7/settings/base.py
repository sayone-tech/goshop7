"""
Django settings for shop7 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.dirname('settings')
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))
URLS_DIRECTORY = os.path.abspath(os.path.join(SETTINGS_DIR,os.path.pardir))
BASE_DIR = os.path.abspath(os.path.join(URLS_DIRECTORY,os.path.pardir))
print "BASE_DIR",BASE_DIR
TEST_PEP8_DIRS = [os.path.dirname(BASE_DIR), ]

DEBUG=False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ka9=k&4z2y!g#2@b&a7v5j-27q8*lt#grjt8e*o6c+-&i7^9ef'

ALLOWED_HOSTS = ['*']
# SECURITY WARNING: don't run with debug turned on in production!



# Application definition
TEST_PEP8_EXCLUDE = ['migrations', ] # Exclude this paths from tests
TEST_PEP8_IGNORE = ['E128', ] # Ignore this tests



INTERNAL_IPS = ('127.0.0.1:8000',)



SITE_ID = 1

STATIC_URL = '/static/'

ROOT_URLCONF = 'shop7.urls'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles'),)

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "templates/oscar"),
    OSCAR_MAIN_TEMPLATE_DIR,
)

WSGI_APPLICATION = 'shop7.wsgi.application'

gettext_noop = lambda s: s
LANGUAGES = (
    ('en', gettext_noop('English')),
#    ('ar', gettext_noop('Arabic')),
    )
LANGUAGE_CODE = 'en'

SSL=False

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



