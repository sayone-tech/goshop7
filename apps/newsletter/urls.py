from django.conf.urls import *
from apps.newsletter.views import *

urlpatterns = patterns(
    'apps.newsletter.views',
    url(r'^subscribe/$', Newsletter.as_view(), name='newsletter'),
    url(r'^$', 'newsletter_subscription', name='newsletter_subscription'),
    url(r'^newsletter/subscribe/confirm/(?P<key>\w+)/$', 'newsletter_subscription_confirm',
        name='newsletter_subscription_confirm'),
    url(r'^newsletter/unsubsribe/confirm/(?P<key>\w+)/$', 'newsletter_unsubscription_confirm',
        name='newsletter_unsubscription_confirm'),
    url(r'^newsletter/unsubsribe/$', NewsletterUnsubscription.as_view(),
        name='newsletter_unsubscription'),)
