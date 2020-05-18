from django import forms
from apps.contact.models import ContactUs
from django.core.mail import EmailMessage
from django.template import Context
from django.template import loader
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.shortcuts import render


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'msg')

    def send_email(self, form_data):
        site = Site.objects.get_current()
        template = loader.get_template('contact/contact_email.html')
        name = form_data.get('name')
        email = form_data.get('email')
        subject = form_data.get('subject')
        msg = form_data.get('msg')
        c = Context({'site': site, 'name': name, 'email': email,
                    'subject': subject, 'message': msg})
        content = template.render(c)
        email = EmailMessage(
            'Contact request recieved', content,
            settings.OSCAR_FROM_EMAIL,
            [settings.OSCAR_FROM_EMAIL], [], headers={})
        email.content_subtype = 'html'
        email.send()

        t = loader.get_template('contact/contact_user_email.html')
        c = Context({'site': site, 'name': name, 'email': email,
                    'subject': subject, 'message': msg})
        rendered = t.render(c)
        text_content = strip_tags(rendered)
        html_content = rendered
        email_obj = EmailMultiAlternatives(
            'Thank you for contacting us', text_content,
            settings.OSCAR_FROM_EMAIL, [form_data.get('email')])
        email_obj.attach_alternative(html_content, "text/html")
        email_obj.send()


class ContactForm2(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject')

    def send_email(self, form_data):
        site = Site.objects.get_current()
        template = loader.get_template('contact/contact_email.html')
        name = form_data.get('name')
        email = form_data.get('email')
        subject = form_data.get('subject')
        msg = 'phone number is the provided subject'
        c = Context({'site': site, 'name': name, 'email': email,
                    'subject': subject, 'message': msg})
        content = template.render(c)
        email = EmailMessage(
            'Contact request recieved', content,
            settings.OSCAR_FROM_EMAIL,
            [settings.OSCAR_FROM_EMAIL], [], headers={})
        email.content_subtype = 'html'
        email.send()

        t = loader.get_template('contact/contact_user_email.html')
        c = Context({'site': site, 'name': name, 'email': email,
                    'subject': subject, 'message': ''})
        rendered = t.render(c)
        text_content = strip_tags(rendered)
        html_content = rendered
        email_obj = EmailMultiAlternatives(
            'Thank you for contacting us', text_content,
            settings.OSCAR_FROM_EMAIL, [form_data.get('email')])
        email_obj.attach_alternative(html_content, "text/html")
        email_obj.send()