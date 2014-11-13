from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from apps.utils.views import get_profile

not_a_demo_user_required = user_passes_test(lambda u: not get_profile(u).groups.filter(name="Demo").exists(),
                                   login_url='/dashboard/')

def not_a_demo_user(view_func):
    decorated_view_func = login_required(not_a_demo_user_required(view_func))
#    def _wrapped_view(request, *args, **kwargs):
#        messages.success(request, _('Demo user has no permission to delete item.'))
    return decorated_view_func