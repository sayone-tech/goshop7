from django.utils.functional import cached_property
from django import template
from oscar.apps.catalogue.models import Product
register = template.Library()


@cached_property
@register.assignment_tag
def offer_products():
    print "sssssssssssssssssssssssssssssssssssss"
    offers=Product.objects.filter(is_discountable=True)
    print "offersssssssssssssssssssssssssssssssssssss",offers
    return offers