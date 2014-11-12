from django.conf.urls import patterns, url
from oscar.apps.dashboard.vouchers import views
from oscar.apps.dashboard.vouchers.app import VoucherDashboardApplication as CoreVoucherDashboardApplication

from apps.utils.decorator import not_a_demo_user


class VoucherDashboardApplication(CoreVoucherDashboardApplication):
    
    def get_urls(self):
        urls = [
            url(r'^$', self.list_view.as_view(), name='voucher-list'),
            url(r'^create/$', self.create_view.as_view(),
                name='voucher-create'),
            url(r'^update/(?P<pk>\d+)/$', self.update_view.as_view(),
                name='voucher-update'),
            url(r'^delete/(?P<pk>\d+)/$', not_a_demo_user(self.delete_view.as_view()),
                name='voucher-delete'),
            url(r'^stats/(?P<pk>\d+)/$', self.stats_view.as_view(),
                name='voucher-stats'),
        ]
        return self.post_process_urls(patterns('', *urls))


application = VoucherDashboardApplication()
