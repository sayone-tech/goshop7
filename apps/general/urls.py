from django.conf.urls import patterns,url
from django.conf.urls import include
from apps.general.views import *

urlpatterns = patterns('apps.general.views',
                        url(r'^basket/delete-line/$',BasketRemoveView.as_view(),name='remove_line'),
                        url(r'^advancedsearch/$',AutoCompSearchView.as_view(),name='advanced_search'),
                        url(r'^whish_delete_line/$',WishlistLineDeleteView.as_view(),name='whish_delete_line'),
                        )