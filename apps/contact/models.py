import datetime

from django.db import models

from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class ContactUs(models.Model):
    name = models.CharField(('Nmae'), max_length=100)
    email = models.EmailField(('Email'), max_length=100)
    subject = models.CharField(('Subject'), max_length=255)
    contact_date = models.DateTimeField(('Contact date'),
                                        null=True, blank=True, default=datetime.datetime.now())
    msg = models.TextField(('Message'), default=False)
    user_ip = models.GenericIPAddressField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    browser_information = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')
