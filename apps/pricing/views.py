import json

from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.pricing.forms import PricingForm
from apps.pricing.models import DemoPricing


class PricingView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PricingView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            ctx = {}
            type = self.request.POST.get('type')
            if type == 'pricing':
                id = self.request.POST.get('pricing_id')
                pricing = DemoPricing.objects.get(id=id)
                ctx['price'] = pricing.price
                ctx['discount_price'] = pricing.discount_price
            else:
                pricing_form = PricingForm(request.POST)
                if pricing_form.is_valid():
                    pricing_data = pricing_form.save()
                    pricing_form.send_email(pricing_data)
                    ctx['status'] = 'success'
                else:
                    ctx['errors'] = pricing_form.errors
        return HttpResponse(json.dumps(ctx, cls=DjangoJSONEncoder), mimetype='application/json')
