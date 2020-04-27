"""
WSGI config for shop7 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os,sys
sys.path.append('/home/sayonetech/webapps/shop/virtual/lib/python2.7/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop7.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
