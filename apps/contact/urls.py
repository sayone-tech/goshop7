from django.conf.urls import patterns,url
from django.conf.urls import include

from apps.contact.views import *

urlpatterns = patterns('apps.contact.views',
                        url(r'^contact/$',ContactView.as_view(),name='contactus'))