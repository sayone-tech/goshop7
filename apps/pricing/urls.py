from django.conf.urls import patterns, url
from django.conf.urls import include

from apps.pricing.views import *

urlpatterns = patterns('apps.pricing.views',
                        url(r'^pricing/$', PricingView.as_view(), name='pricing'))
