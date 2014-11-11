from django.template import Library
from django.core.cache import cache

from apps.socialmedias.models import SocialLinks
register = Library()


@register.assignment_tag
def get_social_links():
    social_links = SocialLinks.get_published()
    return social_links
