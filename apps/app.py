from apps.app_oscar import Shop

from apps.checkout.app import application as checkout_app
from apps.catalogue.app import application as catalogue_app
#from apps.dashboard.app import application as dashboard_app

class BaseApplication(Shop):
    checkout_app = checkout_app
    catalogue_app = catalogue_app
#    dashboard_app = dashboard_app


application = BaseApplication()