import datetime

from django.db import models


class DemoPricing(models.Model):
    title = models.CharField(max_length=50,)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.title


class Features(models.Model):
    demopricing = models.ForeignKey(DemoPricing, related_name='demo_features')
    feature = models.CharField(max_length=100)


class ActiveDemoPricing(models.Model):
    demopricing = models.ForeignKey(DemoPricing, related_name='active_demos')
    name = models.CharField(('Nmae'), max_length=100)
    email = models.EmailField(('Email'), max_length=100)
    mobile_no = models.CharField(('Mobile Number'), max_length=255)
    message = models.TextField(('Message'))
    activated_date = models.DateTimeField(('Acitvated date'),
        null=True, blank=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.demopricing.title
