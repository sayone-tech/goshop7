from django.conf.urls import patterns, url
from oscar.apps.dashboard.pages import views
from oscar.apps.dashboard.pages.app import FlatPageManagementApplication as CoreFlatPageManagementApplication

from apps.utils.decorator import not_a_demo_user


class FlatPageManagementApplication(CoreFlatPageManagementApplication):

    def get_urls(self):
        """
        Get URL patterns defined for flatpage management application.
        """
        urls = [
            url(r'^$', self.list_view.as_view(), name='page-list'),
            url(r'^create/$', self.create_view.as_view(), name='page-create'),
            url(r'^update/(?P<pk>[-\w]+)/$',
                self.update_view.as_view(), name='page-update'),
            url(r'^delete/(?P<pk>\d+)/$',
                not_a_demo_user(self.delete_view.as_view()), name='page-delete')
        ]
        return self.post_process_urls(patterns('', *urls))


application = FlatPageManagementApplication()
