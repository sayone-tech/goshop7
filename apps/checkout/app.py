from oscar.apps.checkout.app import CheckoutApplication as CoreCheckoutApplication

from apps.checkout import views


class CheckoutApplication(CoreCheckoutApplication):

    payment_method_view = views.PaymentMethodView
    payment_details_view = views.PaymentDetailsView

application = CheckoutApplication()
