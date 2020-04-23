from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User

class AdminForceRedirect:
    def process_view(self, request,view_func, view_args, view_kwargs ):
        if request.user.groups.filter(name="Demo").exists() and ('shop7-admin' in request.path):
            logout(request)
        else:
            pass