from django.conf.urls import *

from apps.oscar_cod import views


urlpatterns = patterns('',
    # Views for normal flow that starts on the basket page
    url(r'^payment/$',
        views.CodPaymentDetailsView.as_view(preview=True),
        name='cod_payment'),
)
