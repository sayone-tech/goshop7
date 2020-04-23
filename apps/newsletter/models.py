from django.db import models
import random
import string
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import Context
from django.template import loader
from django.contrib.sites.models import Site
# from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


class NewsletterSubscription(models.Model):
    email = models.EmailField(('Email'), max_length=100)
    date_created = models.DateTimeField(('DateTime'), null=True, blank=True)
    hash_key = models.CharField(('Hash Key'), max_length=100, null=True, blank=True)
    confirm = models.BooleanField(('Confirm'), default=False)

    class Meta:
        ordering = ('email', )
        verbose_name = _('newsletter subscription')
        verbose_name_plural = _('newsletter subscriptions')

    def save(self, * args, ** kwargs):
        if not self.hash_key:
            self.hash_key = self.random_key()
        super(NewsletterSubscription, self).save(*args, ** kwargs)

    def random_key(self):
        alphabet = [c for c in string.letters + string.digits if ord(c) < 128]
        return ''.join([random.choice(alphabet) for x in xrange(30)])


class Newsletter(models.Model):
    title = models.CharField(('Title'), max_length=100)
    message = RichTextField(('Message'))
    date = models.DateField(('Date Field'), auto_now_add=True)
    send = models.BooleanField(_('Send Now?'), default=False)
    is_sent = models.BooleanField(_('Is Sent'), default=False, editable=False)

    class Meta:
        verbose_name = _('Newsletter')
        verbose_name_plural = _('Newsletters')

    def send_newsletter(self):
        subscribers = NewsletterSubscription.objects.filter(confirm=True)
        site = Site.objects.get_current()
        title = "Shop7 NewsLetter"
#        title1=GeneralSettings.objects.get(site=site)
        for sub in subscribers:
            title = self.title
            message = self.message
            template = loader.get_template('newsletter/newsletter_content.html')
            c = Context({'site': site, 'title': title, 'message': message, 'key': sub.hash_key})
            content = template.render(c)
            email = EmailMessage('[%s]%s' % (site.name, 'Shop 7'), content,
                                 settings.DEFAULT_FROM_EMAIL, [sub.email], [], headers = {})
            email.content_subtype = 'html'
            email.send()

    def save(self, *args, **kwargs):
        # Call super method 'save'
        super(Newsletter, self).save(*args, **kwargs)
        if (self.send == True):
            try:
                self.send_newsletter()
                # Set send_status to True to prevent further sending of this newsletter
                self.is_sent = True
            except:
                self.is_sent = False
            self.send = False
            self.save()
