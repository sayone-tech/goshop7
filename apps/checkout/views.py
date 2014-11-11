import six
import logging
from django.shortcuts import redirect
from django.conf import settings
from django import http
from django.contrib import messages
from django.contrib.auth import login
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

from oscar.apps.checkout import views as checkout_views
from oscar.core.loading import get_model
from oscar.apps.shipping.methods import NoShippingRequired
from oscar.core.loading import get_class, get_classes

ShippingAddressForm, GatewayForm \
    = get_classes('checkout.forms', ['ShippingAddressForm', 'GatewayForm'])
OrderCreator = get_class('order.utils', 'OrderCreator')
UserAddressForm = get_class('address.forms', 'UserAddressForm')
Repository = get_class('shipping.repository', 'Repository')
AccountAuthView = get_class('customer.views', 'AccountAuthView')
RedirectRequired, UnableToTakePayment, PaymentError \
    = get_classes('payment.exceptions', ['RedirectRequired',
                                         'UnableToTakePayment',
                                         'PaymentError'])
UnableToPlaceOrder = get_class('order.exceptions', 'UnableToPlaceOrder')
OrderPlacementMixin = get_class('checkout.mixins', 'OrderPlacementMixin')
CheckoutSessionMixin = get_class('checkout.session', 'CheckoutSessionMixin')

Order = get_model('order', 'Order')
ShippingAddress = get_model('order', 'ShippingAddress')
CommunicationEvent = get_model('order', 'CommunicationEvent')
PaymentEventType = get_model('order', 'PaymentEventType')
PaymentEvent = get_model('order', 'PaymentEvent')
UserAddress = get_model('address', 'UserAddress')
Basket = get_model('basket', 'Basket')
Email = get_model('customer', 'Email')
CommunicationEventType = get_model('customer', 'CommunicationEventType')

# Standard logger for checkout events
logger = logging.getLogger('oscar.checkout')

# ==============
# Payment method
# ==============


class PaymentMethodView(checkout_views.PaymentMethodView):
    """
    View for a user to choose which payment method(s) they want to use.

    This would include setting allocations if payment is to be split
    between multiple sources. It's not the place for entering sensitive details
    like bankcard numbers though - that belongs on the payment details view.
    """
    template_name = 'checkout/payment_methods.html'

    def get(self, request, *args, **kwargs):
        # By default we redirect straight onto the payment details view. Shops
        # that require a choice of payment method may want to override this
        # method to implement their specific logic.
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        method_code = request.POST.get('payment_method', None)
        if not method_code:
            messages.error(self.request, _("Please select a payment method."))
            return http.HttpResponseRedirect(reverse('checkout:payment-method'))
        self.checkout_session.pay_by(method_code)
        if method_code == 'cod':
            return http.HttpResponseRedirect(reverse('checkout:preview'))
        return http.HttpResponseRedirect(reverse('checkout:preview'))
        return self.get_success_response()

    def get_available_payment_methods(self):
        """All available payment methods are displayed to customer, to select a choice
        Returns all applicable payment method objects
        for a given basket.
        """
        return settings.OSCAR_PAYMENT_METHODS

    def get_context_data(self, **kwargs):
        kwargs = super(PaymentMethodView, self).get_context_data(**kwargs)
        kwargs['methods'] = self.get_available_payment_methods()
        kwargs['payment_method'] = self.checkout_session.payment_method()
        return kwargs


class PaymentDetailsView(checkout_views.PaymentDetailsView):
    """
    For taking the details of payment and creating the order.

    This view class is used by two separate URLs: 'payment-details' and
    'preview'. The `preview` class attribute is used to distinguish which is
    being used.

    If sensitive details are required (eg a bankcard), then the payment details
    view should submit to the preview URL and a custom implementation of
    `validate_payment_submission` should be provided.

    - If the form data is valid, then the preview template can be rendered with
      the payment-details forms re-rendered within a hidden div so they can be
      re-submitted when the 'place order' button is clicked. This avoids having
      to write sensitive data to disk anywhere during the process. This can be
      done by calling `render_preview`, passing in the extra template context
      vars.

    - If the form data is invalid, then the payment details templates needs to
      be re-rendered with the relevant error messages. This can be done by
      calling `render_payment_details`, passing in the form instances to pass
      to the templates.

    The class is deliberately split into fine-grained methods, responsible for
    only one thing.  This is to make it easier to subclass and override just
    one component of functionality.

    All projects will need to subclass and customise this class as no payment
    is taken by default.
    """

    def get(self, request, *args, **kwargs):
        payment_method = self.checkout_session.payment_method()
        if not payment_method:
            messages.error(self.request, _("Please select a payment method."))
            return http.HttpResponseRedirect(reverse('checkout:payment-method'))
#        if payment_method=='paypal':
#            return redirect('paypal-redirect')
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        if self.preview:
            if request.POST.get('action', '') == 'place_order':
                payment_method = self.checkout_session.payment_method()
                print payment_method
                if payment_method == 'credit_card':
                    return redirect('to_cyber')
                if payment_method == 'paypal':
                    return redirect('paypal-redirect')
                submission = self.build_submission()
                return self.submit(**submission)

            return self.render_preview(request)

        # Posting to payment-details isn't the right thing to do
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        ctx['payment_method'] = self.checkout_session.payment_method()
        return ctx
