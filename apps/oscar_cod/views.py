from django.conf import settings 

from apps.checkout import views as checkout_views
from oscar.apps.payment.models import SourceType, Source
    
class CodPaymentDetailsView(checkout_views.PaymentDetailsView):
    template_name_preview = 'checkout/preview.html'
    preview = True

    # We don't have the usual pre-conditions (Oscar 0.7+)
    pre_conditions = ()

    def handle_payment(self, order_number, total, **kwargs):
        """
        Complete payment with cod - this calls the 'DoExpressCheckout'
        method to capture the money from the initial transaction.
        """
        # Record payment source and event
        source_type, is_created = SourceType.objects.get_or_create(
            name='Cash on Delivery')
        source = Source(source_type=source_type,
                        currency=settings.OSCAR_DEFAULT_CURRENCY,
                        amount_allocated=total.incl_tax,
                        amount_debited=0)
        self.add_payment_source(source)
        self.add_payment_event('Allocated', total.incl_tax,
                               reference='COD'+str(order_number))