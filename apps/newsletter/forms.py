from django import forms
from apps.newsletter.models import NewsletterSubscription


class NewsLetterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        exclude = ('date_created', 'hash_key', 'confirm')
