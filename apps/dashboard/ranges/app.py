from django.conf.urls import patterns, url
from oscar.apps.dashboard.ranges import views
from oscar.apps.dashboard.ranges.app import RangeDashboardApplication as CoreRangeDashboardApplication

from apps.utils.decorator import not_a_demo_user


class RangeDashboardApplication(CoreRangeDashboardApplication):

    def get_urls(self):
        urlpatterns = patterns(
            '',
            url(r'^$', self.list_view.as_view(), name='range-list'),
            url(r'^create/$', self.create_view.as_view(), name='range-create'),
            url(r'^(?P<pk>\d+)/$', self.update_view.as_view(),
                name='range-update'),
            url(r'^(?P<pk>\d+)/delete/$', not_a_demo_user(self.delete_view.as_view()),
                name='range-delete'),
            url(r'^(?P<pk>\d+)/products/$', self.products_view.as_view(),
                name='range-products'),
            url(r'^(?P<pk>\d+)/reorder/$', self.reorder_view.as_view(),
                name='range-reorder'),
        )
        return self.post_process_urls(urlpatterns)


application = RangeDashboardApplication()
