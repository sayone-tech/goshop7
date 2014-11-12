import random

from django import forms
from apps.pricing.models import ActiveDemoPricing
from django.core.mail import EmailMessage
from django.template import Context
from django.template import loader
from django.conf import settings
from django.contrib.sites.models import Site


class PricingForm(forms.ModelForm):

    class Meta:
        model = ActiveDemoPricing

    def __init__(self, *args, **kwargs):
        super(PricingForm, self).__init__(*args, **kwargs)
        self.fields['demopricing'].widget.attrs['class'] = 'package-drop'
        self.fields['demopricing'].empty_label = None

    def send_email(self, pricing_data):
        site = Site.objects.get_current()
        template = loader.get_template('contact/pricing_email.html')
        random_number = random.randint(1000, 9999)
        order_no = "OD" + str(random_number)
        c = Context({'site': site, 'pricing_data': pricing_data, 'order_no': order_no, })
        content = template.render(c)
        email = EmailMessage('[%s]' % (site.name), content, settings.DEFAULT_FROM_EMAIL,\
                            [pricing_data.email, 'hello@goshop7.com'], [], headers={})
        email.content_subtype = 'html'
        email.send()
