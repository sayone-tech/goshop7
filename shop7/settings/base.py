"""
Django settings for shop7 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from oscar import get_core_apps
#BASE_DIR = os.path.dirname('settings')
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))
URLS_DIRECTORY = os.path.abspath(os.path.join(SETTINGS_DIR,os.path.pardir))
BASE_DIR = os.path.abspath(os.path.join(URLS_DIRECTORY,os.path.pardir))

TEST_PEP8_DIRS = [os.path.dirname(BASE_DIR), ]

DEBUG=False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ka9=k&4z2y!g#2@b&a7v5j-27q8*lt#grjt8e*o6c+-&i7^9ef'



TEST_PEP8_EXCLUDE = ['migrations', ] # Exclude this paths from tests
TEST_PEP8_IGNORE = ['E128', ] # Ignore this tests

ALLOWED_HOSTS = ['*','127.0.0.1:8000','127.0.0.1:9000']
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

INSTALLED_APPS = [
    'djangocms_admin_style',
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
    'test_pep8',
    'apps.cybersource',
    'allauth',
    'allauth.account',
    'admin_shortcuts',
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
    'apps.customer',
    'apps.search',
    'lxml',
#    'apps.customer',
    'apps.dashboard.catalogue',
    'apps.dashboard.offers',
    'apps.dashboard.pages',
    'apps.dashboard.partners',
#    'apps.dashboard.promotions',
    'apps.dashboard.ranges',
    'apps.dashboard.reviews',
    'apps.dashboard.users',
    'apps.dashboard.vouchers',
    'apps.newsletter',
    'autocomplete_light',
    'debug_toolbar',
    'apps.socialmedias',
    'apps.contact',
    'apps.pricing',
#    'sentry',
#    'raven.contrib.django',
    'raven.contrib.django.raven_compat',
]+ get_core_apps()


RAVEN_CONFIG = {
    'dsn': 'http://321fb5a669604f0e9cb38ce36bfd21c6:eca12dc7b5da4f1eb7a40177e8963b20@127.0.0.1:9000/2',
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'apps.utils.middleware.AdminForceRedirect', # demo user denied to access the admin site
)


DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]



INTERNAL_IPS = ('127.0.0.1:8000',)

ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'shop7-admin:auth_user_changelist',
                'title': 'Users',
            },
        ]
    },

]
ADMIN_SHORTCUTS_SETTINGS = {

    'open_new_window': False,
}

CKEDITOR_UPLOAD_PATH = "media/"

CONFIG_DEFAULTS = {
    'RESULTS_STORE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

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
    "apps.general.context_processors.google_analytics",
    "apps.general.context_processors.demo_pricing_form",
)

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',
    'django.contrib.auth.backends.ModelBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_REDIRECT_URL='/shop/accounts/profile/'



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


CYBERSOURCE_DEFAULT_CURRENCY = 'USD'
CYBERSOURCE_MERCHANT_ID = 'goshop7'
CYBERSOURCE_PASSWORD = 'VoA7SKROKesU+yZu4xVHhyKcGGzyvPENJXx+zikvBrOEIZR8P9kTJJKJR52D289D+NUEta4q4ygK43rE3G1zHICAMNFQb/M7Sov7gmW7rvtguv8jkK0CfF2aqPh7pSKse0M+yVB1qc2OQ4M4myXl4pkm0oagJagKcyqhCc6wizNJ245LAvrqQMpuCvMkpJYJxh3rewGSKAhVq0cjxXAC2swpzxsPqiWdy+cJ+90FbC5MTKQS0JJcviC6K3TjVMVJQFQu11mnf01JJOauu8ZUnV3P6kzD2uI2/WeNczQUhBWmL4DyCpFpcBts8F8XwennoqXBBExu3ukQJ6fuqS/xtQ=='




