"""
Django settings for shop7 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ka9=k&4z2y!g#2@b&a7v5j-27q8*lt#grjt8e*o6c+-&i7^9ef'

# SECURITY WARNING: don't run with debug turned on in production!

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

# Application definition

from oscar import get_core_apps
INSTALLED_APPS = [
    #'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'apps.general',
    'south',
    'mailer',
    'paypal',
    'compressor',
    'apps',
    'ckeditor',
    'apps.cybersource',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin',
    'endless_pagination',
    'apps.checkout',
    'apps.catalogue',
    'apps.basket',
    'apps.search',
    'lxml',
#    'apps.customer',
    'apps.dashboard.catalogue',
    'apps.newsletter',
    'autocomplete_light',
]+ get_core_apps()

SITE_ID = 1

ROOT_URLCONF = 'shop7.urls'

WSGI_APPLICATION = 'shop7.wsgi.application'

CKEDITOR_UPLOAD_PATH = "media/"
#LOGIN_REDIRECT_URL = 'shop/accounts/profile'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
CKEDITOR_UPLOAD_PATH = "media/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SUIT_CONFIG = {
    'ADMIN_NAME': 'Django Suit',
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    }

}

CYBERSOURCE_DEFAULT_CURRENCY = 'USD'
CYBERSOURCE_MERCHANT_ID = 'goshop7'
CYBERSOURCE_PASSWORD = 'VoA7SKROKesU+yZu4xVHhyKcGGzyvPENJXx+zikvBrOEIZR8P9kTJJKJR52D289D+NUEta4q4ygK43rE3G1zHICAMNFQb/M7Sov7gmW7rvtguv8jkK0CfF2aqPh7pSKse0M+yVB1qc2OQ4M4myXl4pkm0oagJagKcyqhCc6wizNJ245LAvrqQMpuCvMkpJYJxh3rewGSKAhVq0cjxXAC2swpzxsPqiWdy+cJ+90FbC5MTKQS0JJcviC6K3TjVMVJQFQu11mnf01JJOauu8ZUnV3P6kzD2uI2/WeNczQUhBWmL4DyCpFpcBts8F8XwennoqXBBExu3ukQJ6fuqS/xtQ=='
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
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

#PAYPAL_CALLBACK_HTTPS=False

#PAYPAL_PAYFLOW_VENDOR_ID = 'tester_1348840829_biz@gmail.com'
#PAYPAL_PAYFLOW_PASSWORD = 'tester@kuwaitnet'
PAYPAL_API_USERNAME = 'vishnu.sayone-facilitator_api1.gmail.com'
PAYPAL_API_PASSWORD = 'V59UVTEQ8H3ML973'
PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AiSPlTNnVWuzcmHDqBWlK3pJqCNk'
PAYPAL_SANDBOX_MODE=True
#PAYPAL_TEST = True
PAYPAL_PAYFLOW_CURRENCY = 'USD'
PAYPAL_CURRENCY = 'USD'
PAYPAL_API_VERSION = '88.0'
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#For Oscar

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',

    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',
    'django.contrib.auth.backends.ModelBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_REDIRECT_URL='/shop/accounts/profile/'

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

ENDLESS_PAGINATION_LOADING='/static/assets/global/img/loading-spinner-blue.gif/'

from oscar.defaults import *

#simpleEngine
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        'EXCLUDED_INDEXES':
            ['oscar.apps.search.search_indexes.ProductIndex',]
    },
}

#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8983/solr',
#        'INCLUDE_SPELLING': True,
#        'EXCLUDED_INDEXES':
#            ['oscar.apps.search.search_indexes.ProductIndex',]
#    },
#}

# Haystack settings
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#        'EXCLUDED_INDEXES':
#            ['oscar.apps.search.search_indexes.ProductIndex',]
#    },
#}


from django.utils.translation import ugettext_lazy as _
OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('PayPal'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
    })

OSCAR_SHOP_NAME = 'Shop7'
OSCAR_SHOP_TAGLINE = 'Demo'
OSCAR_DEFAULT_CURRENCY = 'INR'
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_SUCCESS_STATUS = 'Delivered Successfully'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('In Progress', 'Cancelled',),
    'In Progress': ('Delivered Successfully', 'Cancelled',),
    'Delivered Successfully': (),
    'Cancelled': (),
}
OSCAR_LINE_STATUS_PIPELINE = {
    'Pending': ('In Progress', 'Cancelled',),
    'In Progress': ('Delivered Successfully', 'Cancelled',),
    'Delivered Successfully': (),
    'Cancelled': (),
}
#OSCAR_PRODUCTS_PER_PAGE = 1
#oscar custom settings
OSCAR_PAYMENT_METHODS = (
('cod','Cash on Delivery'),
('paypal','Paypal'),
('credit_card','Credit card/Debit card'),
)
#allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True