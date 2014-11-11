from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
from django.conf import settings
from decimal import Decimal
from xml.dom.minidom import parseString
import lxml.html as lh
from oscar.core.loading import get_class, get_classes
import urllib2
RedirectRequired, UnableToTakePayment, PaymentError = get_classes(
    'payment.exceptions', ['RedirectRequired', 'UnableToTakePayment', 'PaymentError'])

OrderNumberGenerator = get_class('order.utils','OrderNumberGenerator')
from apps.checkout.views import PaymentDetailsView
from apps.cybersource.forms import CybersourceForm
from apps.cybersource.models import CyberTransaction
from apps.cybersource.cyber import Processor

class ToCybersourceView(PaymentDetailsView):
    template_name = 'cybersource/cyber_form.html'
    form_class = CybersourceForm
    cyber_kwargs = {}
    
    def get_context_data(self, **kwargs):
        kwargs['form'] = self.form_class(initial={'accountNumber':4111111111111111,'firstName':'Test Name','cvNumber':123,})
        return kwargs
    
    def post(self, request, *args, **kwargs):
        # Need to check that this code is valid for this user
        self.form = self.form_class(request.POST)
        if self.form.is_valid():
            submission = self.build_submission()
            basket = submission['basket']
            total = submission['order_total']
            total_incl_tax, total_excl_tax = total.incl_tax,total.excl_tax,
            #payment
            self.cyber_kwargs['currency'] = settings.CYBERSOURCE_DEFAULT_CURRENCY
            order_number = self.generate_order_number(basket)
            self.cyber_kwargs['order_number'] = order_number
            url="https://www.google.com/finance/converter?a=%s&from=%s&to=%s"% (total_incl_tax,'INR','USD')
            file = urllib2.urlopen(url)
            data = file.read()
            file.close()
            dom = lh.parse(urllib2.urlopen(url))
            blurb=dom.find('.//span[@class="bld"]').text_content()
            #amount=Decimal(blurb.split[' '])
            amount=blurb.replace("USD","")
            total_incl_tax=amount
            self.cyber_kwargs['total'] = total_incl_tax
            #card
            form = self.form
            self.cyber_kwargs['account_number'] = form.cleaned_data.get('accountNumber')
            self.cyber_kwargs['exp_month'] = form.cleaned_data.get('expirationMonth')
            self.cyber_kwargs['exp_year'] = form.cleaned_data.get('expirationYear')
            self.cyber_kwargs['cvv'] = form.cleaned_data.get('cvNumber')
            self.cyber_kwargs['card_type'] = form.cleaned_data.get('cardType')
            #billInfo
            bill_data = self.get_shipping_address(self.request.basket)
            self.cyber_kwargs['title'] = bill_data.title
            self.cyber_kwargs['first_name'] = bill_data.first_name
            self.cyber_kwargs['last_name'] = bill_data.last_name
            self.cyber_kwargs['address1'] = bill_data.line1
            self.cyber_kwargs['address2'] = bill_data.line2
            self.cyber_kwargs['city'] = bill_data.line4
            self.cyber_kwargs['state'] = bill_data.state
            self.cyber_kwargs['zipcode'] = bill_data.postcode
            self.cyber_kwargs['country'] = bill_data.country
            if request.user.is_authenticated():
                self.cyber_kwargs['cid'] = request.user.id
                self.cyber_kwargs['email'] = request.user.email
            self.cyber_kwargs['phone_number'] = ''
            self.freeze_basket(submission['basket'])
            cyber = Processor(**self.cyber_kwargs)
            cyper_transaction = cyber.do_payment()
            if cyper_transaction.reasonCode == 100:
                self.checkout_session.set_payment_id(cyper_transaction.requestID)
                return self.submit(**submission)
            else:
                basket.thaw()
                return HttpResponseRedirect('%s?cyberID=%s&order=%s' %(reverse('cyber_error'),cyper_transaction.id,order_number))
        else:
            print self.form.errors,'errors'
        context = self.get_context_data(*args, **kwargs)
        context['form']=self.form
        return self.render_to_response(context)


def cyber_error(request):
    error=''
    tr=None
    cyber_id=request.REQUEST.get('cyberID')
    order_number=request.REQUEST.get('order')
    if cyber_id and order_number:
        tr=get_object_or_404(CyberTransaction,id=cyber_id,order_number=order_number)
        error=tr.error_text
    else:
        return HttpResponseRedirect(reverse('to_cyber'))
    return render_to_response('cybersource/error.html', {'error':error,'tr':tr}, RequestContext(request))