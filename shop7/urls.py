import autocomplete_light
autocomplete_light.autodiscover()
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.functional import curry
from apps.app import application
from apps.dashboard.app import dashapplication
from oscar.core.loading import get_class
from oscar.app import Shop
from oscar.core.application import Application

admin.autodiscover()

class Shop(Application):
    name = None
    dashboard_app = get_class('dashboard.app', 'application')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shop7.views.home', name='home'),   
    url(r'^$', 'apps.catalogue.views.onepage_view',name='main_home'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^cybersource/', include('apps.cybersource.urls')),
    url(r'^shop7-admin/', include(admin.site.urls)),
    url(r'^cod/', include('apps.oscar_cod.urls')),
    url(r'^shop/', include(application.urls)),
    (r'^dashboard/', include(dashapplication.urls)),
    (r'^checkout/paypal/', include('paypal.express.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^newsletter/',include('apps.newsletter.urls')),
    url(r'^',include('apps.contact.urls')),
    url(r'^',include('apps.general.urls')),
    url(r'^',include('apps.pricing.urls')),
    (r'^accounts/', include('allauth.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)

urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes': False}),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = curry('apps.general.views.custom_404', template_name='404.html')
