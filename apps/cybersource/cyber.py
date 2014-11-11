from random import randrange

import suds
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
from django.conf import settings
from models import CyberTransaction
# import logging
# logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)


class CyberSourceBaseException(Exception):
    def __init__(self, error_code, value):
        self.error_code = error_code
        self.value = value

    def __unicode__(self):
        return "{0} (Error code: {1})".format(repr(self.value), self.error_code)

    def __str__(self):
        return self.__unicode__()


class CyberScourceError(CyberSourceBaseException):
    pass


class CyberScourceFailure(CyberSourceBaseException):
    pass


class SchemaValidationError(CyberSourceBaseException):
    def __init__(self):
        self.error_code = -1
        self.value = "suds encountered an error validating your data against this service\
            's WSDL schema. Please double-check for missing or invalid values, filling all\
            required fields."


CYBERSOURCE_RESPONSES = {
    '100': 'Successful transaction.',
    '101': 'The request is missing one or more required fields.',
    '102': 'One or more fields in the request contains invalid data.',
    '104': 'The merchantReferenceCode sent with this authorization request matches the\
        merchantReferenceCode of another authorization request that you sent in the\
        last 15 minutes.',
    '150': 'Error: General system failure. ',
    '151': 'Error: The request was received but there was a server timeout. This error does\
        not include timeouts between the client and the server.',
    '152': 'Error: The request was received, but a service did not finish running in time.',
    '201': 'The issuing bank has questions about the request. You do not receive an authorization\
        code in the reply message, but you might receive one verbally by calling the processor.',
    '202': 'Expired card. You might also receive this if the expiration date you provided does\
        not match the date the issuing bank has on file.',
    '203': 'General decline of the card. No other information provided by the issuing bank.',
    '204': 'Insufficient funds in the account.',
    '205': 'Stolen or lost card.',
    '207': 'Issuing bank unavailable.',
    '208': 'Inactive card or card not authorized for card-not-present transactions.',
    '210': 'The card has reached the credit limit. ',
    '211': 'Invalid card verification number.',
    '221': 'The customer matched an entry on the processor\'s negative file.',
    '231': 'Invalid account number.',
    '232': 'The card type is not accepted by the payment processor.',
    '233': 'General decline by the processor.',
    '234': 'There is a problem with your CyberSource merchant configuration.',
    '235': 'The requested amount exceeds the originally authorized amount. Occurs, for example, if\
        you try to capture an amount larger than the original authorization amount.\
        This reason code\
        only applies if you are processing a capture through the API.',
    '236': 'Processor Failure',
    '238': 'The authorization has already been captured. This reason code only applies if you\
        are processing a capture through the API.',
    '239': 'The requested transaction amount must match the previous transaction amount. This\
        reason code only applies if you are processing a capture or credit through the API.',
    '240': 'The card type sent is invalid or does not correlate with the credit card number.',
    '241': 'The request ID is invalid. This reason code only applies when you are processing\
        a capture or credit through the API.',
    '242': 'You requested a capture through the API, but there is no corresponding, unused\
        authorization record. Occurs if there was not a previously successful authorization request\
        or if the previously successful authorization has already been used by\
        another capture request.\
        This reason code only applies when you are processing a capture through the API.',
    '243': 'The transaction has already been settled or reversed.',
    '246': 'The capture or credit is not voidable because the capture or credit information has\
        already been submitted to your processor. Or, you requested a void for a\
        type of transaction that\
        cannot be voided. This reason code applies only if you are processing a\
        void through the API.',
    '247': 'You requested a credit for a capture that was previously voided. This reason code applies\
        only if you are processing a void through the API.',
    '250': 'Error: The request was received, but there was a timeout at the payment processor.',
    '520': 'The authorization request was approved by the issuing bank but declined by CyberSource based\
        on your Smart Authorization settings.',
}


class Processor(object):

    def __init__(self, *args, **kwargs):
        # Test server
        self.client = Client(
            'https://ics2wstest.ic3.com/commerce/1.x/transactionProcessor/CyberSourceTransaction_1.85.wsdl')

        self.password = settings.CYBERSOURCE_PASSWORD
        self.merchantid = settings.CYBERSOURCE_MERCHANT_ID
        self.kwargs = kwargs

    def create_headers(self):
        wssens = (
            'wsse', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd')
        mustAttribute = Attribute('SOAP-ENV:mustUnderstand', '1')

        security = Element('Security', ns=wssens)
        security.append(mustAttribute)
        security.append(Attribute(
            'xmlns:wsse', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd'))

        usernametoken = Element('UsernameToken', ns=wssens)

        username = Element('Username', ns=wssens).setText(self.merchantid)

        passwordType = Attribute(
            'Type', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile-1.0#PasswordText')
        password = Element('Password', ns=wssens).setText(self.password)
        password.append(passwordType)

        usernametoken.append(username)
        usernametoken.append(password)

        security.append(usernametoken)

        self.client.set_options(soapheaders=security)

    def run_transaction(self):
        try:

            options = dict(
                merchantID=self.merchantid,
                merchantReferenceCode=randrange(0, 100),
                billTo=self.bill_to,
                purchaseTotals=self.payment,
            )

            if getattr(self, 'card', None):
                ccAuthService = self.client.factory.create('ns0:ccAuthService')
                ccAuthService._run = 'true'

                options['card'] = self.card
                options['ccAuthService'] = ccAuthService

            if getattr(self, 'check', None):
                ecDebitService = self.client.factory.create('ns0:ecDebitService')
                ecDebitService._run = 'true'

                options['check'] = self.check
                options['ecDebitService'] = ecDebitService

            self.response = self.client.service.runTransaction(**options)
        except suds.WebFault:
            raise SchemaValidationError()

    def payment_amount(self, **kwargs):
        '''
            currency = None
            discountAmount = None
            taxAmount = None
            dutyAmount = None
            grandTotalAmount = None
            freightAmount = None
            foreignAmount = None
            foreignCurrency = None
            exchangeRate = None
            exchangeRateTimeStamp = None
            additionalAmountType0 = None
            additionalAmount0 = None
            additionalAmountType1 = None
            additionalAmount1 = None
            additionalAmountType2 = None
            additionalAmount2 = None
            additionalAmountType3 = None
            additionalAmount3 = None
            additionalAmountType4 = None
            additionalAmount4 = None
            serviceFeeAmount = None
        '''
        kwargs = self.kwargs
#        kwargs['currency'] = 'USD'
#        kwargs['total'] = 12.50

        currency = kwargs.get('currency')
        grandTotalAmount = kwargs.get('total')

        self.payment = self.client.factory.create('ns0:PurchaseTotals')
        self.payment.currency = currency
        self.payment.grandTotalAmount = grandTotalAmount

    def set_card_info(self, **kwargs):
        '''
            fullName = None
            accountNumber = None
            expirationMonth = None
            expirationYear = None
            cvIndicator = None
            cvNumber = None
            cardType = None
            issueNumber = None
            startMonth = None
            startYear = None
            pin = None
            accountEncoderID = None
            bin = None
        '''
        kwargs = self.kwargs
        accountNumber = kwargs.get('account_number')
        expirationMonth = kwargs.get('exp_month')
        expirationYear = kwargs.get('exp_year')
        cvNumber = kwargs.get('cvv')
        cardType = kwargs.get('card_type')

        # if not all([fullName, accountNumber, expirationMonth, expirationYear, cvNumber]):
        #     raise CyberScourceError('', 'Not all credit card info was gathered')

        self.card = self.client.factory.create('ns0:Card')

        self.card.accountNumber = accountNumber
        self.card.expirationMonth = expirationMonth
        self.card.expirationYear = expirationYear
        self.card.cvIndicator = 1
        self.card.cvNumber = cvNumber
        self.card.cardType = cardType

    def billing_info(self, **kwargs):
        '''
            title = None
            firstName = None
            middleName = None
            lastName = None
            suffix = None
            buildingNumber = None
            street1 = None
            street2 = None
            street3 = None
            street4 = None
            city = None
            county = None
            state = None
            postalCode = None
            country = None
            company = None
            companyTaxID = None
            phoneNumber = None
            email = None
            ipAddress = None
            customerPassword = None
            ipNetworkAddress = None
            hostname = None
            domainName = None
            dateOfBirth = None
            driversLicenseNumber = None
            driversLicenseState = None
            ssn = None
            customerID = None
            httpBrowserType = None
            httpBrowserEmail = None
            httpBrowserCookiesAccepted = None
            nif = None
            personalID = None
            language = None
            name = None
        '''
        kwargs = self.kwargs
        title = kwargs.get('title')
        firstName = kwargs.get('first_name')
        lastName = kwargs.get('last_name')
        street1 = kwargs.get('address1')
        street2 = kwargs.get('address2')
        city = kwargs.get('city')
        state = kwargs.get('state')
        postalCode = kwargs.get('zipcode')
        country = kwargs.get('country', 'US')
        customerID = kwargs.get('cid')
        email = kwargs.get('email')
        phoneNumber = kwargs.get('phone_number')

        self.bill_to = self.client.factory.create('ns0:BillTo')

        self.bill_to.title = title
        self.bill_to.firstName = firstName
        self.bill_to.lastName = lastName
        self.bill_to.street1 = street1
        self.bill_to.street2 = street2
        self.bill_to.city = city
        self.bill_to.state = state
        self.bill_to.postalCode = postalCode
        self.bill_to.country = country
        self.bill_to.customerID = customerID
        self.bill_to.email = email
        self.bill_to.phoneNumber = phoneNumber

    def check_response_for_cybersource_error(self):
        if self.response.reasonCode != 100:
            print self.response
            raise CyberScourceError(
                self.response.reasonCode,
                CYBERSOURCE_RESPONSES.get(str(self.response.reasonCode), 'Unknown Failure'))

    def do_payment(self):
        self.check = None
        self.create_headers()
        self.payment_amount()
        self.set_card_info()
        self.billing_info()
        self.run_transaction()
        cyber = CyberTransaction()
        cyber.order_number = self.kwargs['order_number']
        cyber.merchantID = self.merchantid
#        billinfo
        cyber.title = self.kwargs['title']
        cyber.firstName = self.kwargs['first_name']
        cyber.lastName = self.kwargs['last_name']
        cyber.street1 = self.kwargs['address1']
        cyber.street2 = self.kwargs['address2']
        cyber.city = self.kwargs['city']
        cyber.state = self.kwargs['state']
        cyber.postalCode = self.kwargs['zipcode']
        cyber.country = self.kwargs['country']
        cyber.phoneNumber = self.kwargs['phone_number']
        cyber.email = self.kwargs['email']
        cyber.customerID = self.kwargs['cid']
#        purchase
        cyber.currency = self.kwargs['currency']
        cyber.grandTotalAmount = self.kwargs['total']
#        Card
        cyber.accountNumber = self.kwargs['account_number']
        cyber.expirationMonth = self.kwargs['exp_month']
        cyber.expirationYear = self.kwargs['exp_year']
        cyber.cvIndicator = '1'
        cyber.cvNumber = self.kwargs['cvv']
#        payment
        try:
            cyber.merchantReferenceCode = self.response.merchantReferenceCode
        except AttributeError:
            pass
        cyber.requestID = self.response.requestID
        cyber.decision = self.response.decision
        cyber.reasonCode = self.response.reasonCode
        cyber.requestToken = self.response.requestToken
        try:
            cyber.amount = self.response.ccAuthReply.amount
            cyber.authorizationCode = self.response.ccAuthReply.authorizationCode
            cyber.avsCode = self.response.ccAuthReply.avsCode
            cyber.avsCodeRaw = self.response.ccAuthReply.avsCodeRaw
            cyber.cvCode = self.response.ccAuthReply.cvCode
            cyber.authorizedDateTime = self.response.ccAuthReply.authorizedDateTime
            cyber.processorResponse = self.response.ccAuthReply.processorResponse
            cyber.reconciliationID = self.response.ccAuthReply.reconciliationID
        except AttributeError:
            pass
        cyber.error_text = CYBERSOURCE_RESPONSES.get(str(self.response.reasonCode), 'Unknown Failure')
        cyber.save()
        return cyber
