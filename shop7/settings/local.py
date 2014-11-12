from shop7.settings.base import *
from oscar import get_core_apps

DEBUG=True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop7',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}

PAYPAL_API_USERNAME = 'vishnu.sayone-facilitator_api1.gmail.com'
PAYPAL_API_PASSWORD = 'V59UVTEQ8H3ML973'
PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AiSPlTNnVWuzcmHDqBWlK3pJqCNk'
PAYPAL_SANDBOX_MODE=True
#PAYPAL_TEST = True
PAYPAL_PAYFLOW_CURRENCY = 'USD'
PAYPAL_CURRENCY = 'USD'
PAYPAL_API_VERSION = '88.0'
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True


#EMAIL_SUBJECT_PREFIX = "[Shop7]"

EMAIL_HOST          = 'smtp.webfaction.com'
EMAIL_HOST_PASSWORD = 'x8VbG29r'
EMAIL_HOST_USER     = 'helloshop7'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

OSCAR_FROM_EMAIL = 'Team Shop7 <hello@goshop7.com>'
DEFAULT_FROM_EMAIL = 'Team Shop7 <hello@goshop7.com>'

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-56378954-1'

GOOGLE_ANALYTICS_DOMAIN = 'http://www.goshop7.com/'

GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')