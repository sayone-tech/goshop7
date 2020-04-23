from django.conf.urls import patterns, url
from oscar.apps.dashboard.catalogue import views
from oscar.apps.dashboard.catalogue.app import CatalogueApplication as CoreCatalogueApplication

from apps.utils.decorator import not_a_demo_user


class CatalogueApplication(CoreCatalogueApplication):

    def get_urls(self):
        urls = [
            url(r'^products/(?P<pk>\d+)/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product'),
            url(r'^products/create/$',
                self.product_create_redirect_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/create/(?P<product_class_slug>[\w-]+)/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/(?P<pk>\d+)/delete/$',
                not_a_demo_user(self.product_delete_view.as_view()),
                name='catalogue-product-delete'),
            url(r'^$', self.product_list_view.as_view(),
                name='catalogue-product-list'),
            url(r'^stock-alerts/$', self.stock_alert_view.as_view(),
                name='stock-alert-list'),
            url(r'^product-lookup/$', self.product_lookup_view.as_view(),
                name='catalogue-product-lookup'),
            url(r'^categories/$', self.category_list_view.as_view(),
                name='catalogue-category-list'),
            url(r'^categories/(?P<pk>\d+)/$',
                self.category_detail_list_view.as_view(),
                name='catalogue-category-detail-list'),
            url(r'^categories/create/$', self.category_create_view.as_view(),
                name='catalogue-category-create'),
            url(r'^categories/create/(?P<parent>\d+)$',
                self.category_create_view.as_view(),
                name='catalogue-category-create-child'),
            url(r'^categories/(?P<pk>\d+)/update/$',
                self.category_update_view.as_view(),
                name='catalogue-category-update'),
            url(r'^categories/(?P<pk>\d+)/delete/$',
                not_a_demo_user(self.category_delete_view.as_view()),
                name='catalogue-category-delete'),
            url(r'^product-type/create/$',
                self.product_class_create_view.as_view(),
                name='catalogue-class-create'),
            url(r'^product-types/$',
                self.product_class_list_view.as_view(),
                name='catalogue-class-list'),
            url(r'^product-type/(?P<pk>\d+)/update/$',
                self.product_class_update_view.as_view(),
                name='catalogue-class-update'),
            url(r'^product-type/(?P<pk>\d+)/delete/$',
                not_a_demo_user(self.product_class_delete_view.as_view()),
                name='catalogue-class-delete'),

        ]
        return self.post_process_urls(patterns('', *urls))


application = CatalogueApplication()
