from django.db import models
from django.utils.translation import ugettext_lazy as _


class CyberTransaction(models.Model):
    # Note we don't use a foreign key as the order hasn't been created
    # by the time the transaction takes place
    # order
    order_number = models.CharField(max_length=128, db_index=True)
    # merchant
    merchantID = models.CharField(max_length=45)
    # billTo
    title = models.CharField(max_length=15, blank=True, null=True)
    firstName = models.CharField(max_length=35, blank=True, null=True)
    lastName = models.CharField(max_length=35, blank=True, null=True)
    street1 = models.CharField(max_length=100, blank=True, null=True)
    street2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postalCode = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    customerID = models.CharField(max_length=50, blank=True, null=True)
    # purchaseTotals
    currency = models.CharField(max_length=10)
    grandTotalAmount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    # card
    accountNumber = models.CharField(max_length=70, blank=True, null=True)
    expirationMonth = models.CharField(max_length=10, blank=True, null=True)
    expirationYear = models.CharField(max_length=10, blank=True, null=True)
    cvIndicator = models.CharField(max_length=10, blank=True, null=True)
    cvNumber = models.CharField(max_length=20, blank=True, null=True)
    cardType = models.CharField(max_length=70, blank=True, null=True)
    # payment details
    merchantReferenceCode = models.CharField(max_length=30, blank=True, null=True)
    requestID = models.CharField(max_length=70, blank=True, null=True)
    decision = models.CharField(max_length=20, blank=True, null=True)
    reasonCode = models.CharField(max_length=20, blank=True, null=True)
    requestToken = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    authorizationCode = models.CharField(max_length=70, blank=True, null=True)
    avsCode = models.CharField(max_length=20, blank=True, null=True)
    avsCodeRaw = models.CharField(max_length=20, blank=True, null=True)
    cvCode = models.CharField(max_length=20, blank=True, null=True)
    authorizedDateTime = models.CharField(max_length=100, blank=True, null=True)
    processorResponse = models.CharField(max_length=20, blank=True, null=True)
    reconciliationID = models.CharField(max_length=100, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    error_text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _(u"Cybersource Transaction")
        verbose_name_plural = _(u"Cybersource Transactions")

    def __unicode__(self):
        return u'order-%s | amount-%s' % (self.order_number, self.grandTotalAmount)

    @property
    def result(self):
        return self.decision

    @property
    def transaction_id(self):
        return self.requestID

    @property
    def time(self):
        return self.time_stamp

    @property
    def track_id(self):
        return self.requestToken[:30]

    @property
    def amount(self):
        return self.grandTotalAmount

    @property
    def payment_id(self):
        return self.authorizationCode
