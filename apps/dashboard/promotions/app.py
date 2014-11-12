from django.conf.urls import patterns, url
from oscar.apps.dashboard.promotions import views
from oscar.apps.dashboard.promotions.app import PromotionsDashboardApplication as CorePromotionsDashboardApplication
from oscar.apps.promotions.conf import PROMOTION_CLASSES

from apps.utils.decorator import not_a_demo_user


class PromotionsDashboardApplication(CorePromotionsDashboardApplication):

    def get_urls(self):
        urls = [
            url(r'^$', self.list_view.as_view(), name='promotion-list'),
            url(r'^pages/$', self.page_list.as_view(),
                name='promotion-list-by-page'),
            url(r'^page/(?P<path>/([\w-]+(/[\w-]+)*/)?)$',
                self.page_detail.as_view(), name='promotion-list-by-url'),
            url(r'^create/$',
                self.create_redirect_view.as_view(),
                name='promotion-create-redirect'),
            url(r'^page-promotion/(?P<pk>\d+)/$',
                not_a_demo_user(self.delete_page_promotion_view.as_view()),
                name='pagepromotion-delete')]

        for klass in PROMOTION_CLASSES:
            code = klass.classname()
            urls += [
                url(r'create/%s/' % code,
                    getattr(self, 'create_%s_view' % code).as_view(),
                    name='promotion-create-%s' % code),
                url(r'^update/(?P<ptype>%s)/(?P<pk>\d+)/$' % code,
                    getattr(self, 'update_%s_view' % code).as_view(),
                    name='promotion-update'),
                url(r'^delete/(?P<ptype>%s)/(?P<pk>\d+)/$' % code,
                    not_a_demo_user(getattr(self, 'delete_%s_view' % code).as_view()),
                    name='promotion-delete')]

        return self.post_process_urls(patterns('', *urls))


application = PromotionsDashboardApplication()
