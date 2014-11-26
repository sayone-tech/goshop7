from django import template
from django.conf import settings

register = template.Library()

@register.assignment_tag
def get_banner_img(request):
    """
    change banner image on page refresh
    """
    try:
        request.session['count'] = request.session['count'] + 1
    except:
        request.session['count'] = 1
    if request.session['count']%2 == 0:
        return 1
    else:
        return 0