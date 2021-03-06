from django import template
from django.conf import settings
from oscar.apps.offer.models import ConditionalOffer
from oscar.core.loading import get_model
from oscar.apps.customer import history

Site = get_model('sites', 'Site')

register = template.Library()


@register.assignment_tag
def get_bestselling_products():
    """
    assignment tag listing the best selling products
    """
    Product = get_model('catalogue', 'Product')
    qs = Product.browsable.base_queryset()
    products = qs.order_by('-score')
    return products

@register.assignment_tag
def get_latest_products():
    """
    assignment tag listing the best selling products
    """
    Product = get_model('catalogue', 'Product')
    qs = Product.browsable.base_queryset()
    products = qs.order_by('-date_created')[:30]
    return products

@register.assignment_tag
def get_offers():
    """
    assigment tag to display latest offers
    """
    offers=ConditionalOffer.active.filter(offer_type=ConditionalOffer.SITE)
    return offers

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.simple_tag
def get_payment_method(code):
    return dict(settings.OSCAR_PAYMENT_METHODS)[code]