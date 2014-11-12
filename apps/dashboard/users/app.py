from django.conf.urls import patterns, url
from oscar.apps.dashboard.users import views
from oscar.apps.dashboard.users.app import UserManagementApplication as CoreUserManagementApplication

from apps.utils.decorator import not_a_demo_user


class UserManagementApplication(CoreUserManagementApplication):

    def get_urls(self):
        urls = [
            url(r'^$', self.index_view.as_view(), name='users-index'),
            url(r'^(?P<pk>\d+)/$',
                self.user_detail_view.as_view(), name='user-detail'),
            url(r'^(?P<pk>\d+)/password-reset/$',
                self.password_reset_view.as_view(),
                name='user-password-reset'),

            # Alerts
            url(r'^alerts/$',
                self.alert_list_view.as_view(),
                name='user-alert-list'),
            url(r'^alerts/(?P<pk>\d+)/delete/$',
                not_a_demo_user(self.alert_delete_view.as_view()),
                name='user-alert-delete'),
            url(r'^alerts/(?P<pk>\d+)/update/$',
                self.alert_update_view.as_view(),
                name='user-alert-update'),
        ]
        return self.post_process_urls(patterns('', *urls))


application = UserManagementApplication()
