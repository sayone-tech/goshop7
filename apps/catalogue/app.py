from oscar.apps.catalogue.app import\
    CatalogueApplication as CoreCatalogueApplication
from django.conf.urls import patterns, url, include
from apps.catalogue import views


class CatalogueApplication(CoreCatalogueApplication):
    category_view = views.ProductCategoryView
    detail_view = views.ProductDetailView

    def get_urls(self):
        urlpatterns = super(CatalogueApplication, self).get_urls()
        urls = [
            # has different urlname for legacy reasons
            url(r'^$', self.category_view.as_view(), name='index'),
            url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                self.detail_view.as_view(), name='detail'),
            url(r'^(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                self.category_view.as_view(), name='category'),
            # fallback URL if a user chops of the last part of the URL
            url(r'^(?P<category_slug>[\w-]+(/[\w-]+)*)/$',
                self.category_view.as_view()),
            url(r'^ranges/(?P<slug>[\w-]+)/$',
                self.range_view.as_view(), name='range')]
        urlpatterns += patterns('', *urls)
        return self.post_process_urls(urlpatterns)
application = CatalogueApplication()
