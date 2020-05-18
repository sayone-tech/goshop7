from django.conf.urls import patterns,url
from django.conf.urls import include

from apps.contact.views import *

urlpatterns = patterns('apps.contact.views',
                        url(r'^contact/$',ContactView.as_view(),name='contactus'),
                        url(r'^contact2/$',ContactView2.as_view(),name='contactus2'),
                       )