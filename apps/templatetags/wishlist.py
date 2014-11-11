from django.template import Library
from oscar.apps.wishlists.models import Line,WishList

register = Library()

@register.assignment_tag(takes_context=True)
def wishlist_display(context):
    request=context['request']
    line=''
    wishlist=None
    user=request.user
    try:
        wishlist = WishList.objects.get(owner=user)
    except:
        wishlist=None
    if request.user.is_authenticated() and wishlist:
        line=Line.objects.filter(wishlist=wishlist)
    return line

    