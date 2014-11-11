import datetime
import calendar
from django import forms
from django.db.models import get_model


class CybersourceForm(forms.ModelForm):
    CARD_TYPES = (
        ('', 'Card Type*'),
        ('001', 'Visa'),
        ('002', 'MasterCard'),
        ('003', 'American Express'),
        ('004', 'Discover'),
        ('005', 'Diners Club'),
        ('007', 'JCB'),
        )
    accountNumber = forms.CharField(max_length=70)
    expirationMonth = forms.TypedChoiceField(
        choices=[('', 'Expiration month*')]+[(i, i) for i in range(1, 13)])
    expirationYear = forms.TypedChoiceField(
        choices=[('', 'Expiration year*')]+[(i, i) for i in range(
            datetime.datetime.now().year, datetime.datetime.now().year+51)])
    cardType = forms.TypedChoiceField(choices=CARD_TYPES)
    cvNumber = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super(CybersourceForm, self).__init__(*args, **kwargs)
        self.fields['accountNumber'].widget.attrs['placeholder'] = 'Credit Card number*'
        self.fields['firstName'].widget.attrs['placeholder'] = 'Card Holders Name*'
        self.fields['firstName'].widget.attrs['class'] = 'form-control'
        self.fields['accountNumber'].widget.attrs['class'] = 'form-control'
        self.fields['expirationMonth'].widget.attrs['class'] = 'form-control input-sm'
        self.fields['expirationYear'].widget.attrs['class'] = 'form-control input-sm'
        self.fields['cvNumber'].widget.attrs['placeholder'] = 'Card security code*'
        self.fields['cvNumber'].widget.attrs['class'] = 'form-control'
        self.fields['cardType'].widget.attrs['placeholder'] = 'Card Type*'
        self.fields['cardType'].widget.attrs['class'] = 'form-control input-sm'

    class Meta:
        model = get_model('cybersource', 'CyberTransaction')
        fields = ('cardType', 'firstName', 'accountNumber', 'expirationMonth',
                  'expirationYear', 'cvNumber')

    def clean(self):
        cleaned_data = self.cleaned_data
        expirationMonth = cleaned_data.get('expirationMonth')
        expirationYear = cleaned_data.get('expirationYear')
        if expirationMonth and expirationYear:
            expirationMonth = int(expirationMonth)
            expirationYear = int(expirationYear)
            last_day = calendar.monthrange(expirationYear, expirationMonth)[1]
            expiration_day = datetime.datetime(
                expirationYear, expirationMonth, last_day)+datetime.timedelta(days=1)
            now = datetime.datetime.now()
            if expiration_day <= now:
                raise forms.ValidationError('The card has expired')
        else:
            raise forms.ValidationError('Please select an expiration month and year')
        return cleaned_data
