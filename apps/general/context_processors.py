from django.conf import settings
from django.contrib.sites.models import Site

from apps.pricing.forms import PricingForm
from apps.pricing.models import DemoPricing

def google_analytics(request):
    """
    Use the variables returned in this function to
    render your Google Analytics tracking code template.
    """
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)
    if not settings.DEBUG and ga_prop_id and ga_domain:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
            'GOOGLE_ANALYTICS_DOMAIN': ga_domain,
        }
    return {}

def demo_pricing_form(request):

    site=Site.objects.get(id=1)   
    pricing_list = DemoPricing.objects.all()
    form = PricingForm()
    first_obj=None
    try:
        first_obj = DemoPricing.objects.get(id=1)
        first_price = first_obj.price
        first_discount_price = first_obj.discount_price
    except:
        first_price=0.0
        first_discount_price=0.0
    
    return {'site': site,'pricing_form': form, 'pricing_list':pricing_list, 'first_price': first_price, 'first_discount_price': first_discount_price}