from django.conf.urls import *
from apps.cybersource import views as cyber_view

urlpatterns = patterns("",

        url(r'^get-details/$', cyber_view.ToCybersourceView.as_view(),name='to_cyber'),
        url(r'^error/$', 'apps.cybersource.views.cyber_error',name='cyber_error'),

)
