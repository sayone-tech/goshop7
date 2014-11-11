from oscar.apps.customer.app import CustomerApplication as CoreCustomerApplication
from apps.customer import views


class CustomerApplication(CoreCustomerApplication):

    register_view = views.AccountRegistrationView

application = CustomerApplication()
