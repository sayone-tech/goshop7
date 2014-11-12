from django.conf.urls import patterns, url
from oscar.apps.dashboard.reviews import views
from oscar.apps.dashboard.reviews.app import ReviewsApplication as CoreReviewsApplication

from apps.utils.decorator import not_a_demo_user


class ReviewsApplication(CoreReviewsApplication):

    def get_urls(self):
        urls = [
            url(r'^$', self.list_view.as_view(), name='reviews-list'),
            url(r'^(?P<pk>\d+)/$', self.update_view.as_view(),
                name='reviews-update'),
            url(r'^(?P<pk>\d+)/delete/$', not_a_demo_user(self.delete_view.as_view()),
                name='reviews-delete'),
        ]
        return self.post_process_urls(patterns('', *urls))


application = ReviewsApplication()
