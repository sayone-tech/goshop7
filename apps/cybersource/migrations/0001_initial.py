# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CyberTransaction'
        db.create_table('cybersource_cybertransaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_number', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
            ('merchantID', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phoneNumber', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('customerID', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('grandTotalAmount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('accountNumber', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('expirationMonth', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('expirationYear', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('cvIndicator', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('cvNumber', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('merchantReferenceCode', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('requestID', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('decision', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('reasonCode', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('requestToken', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('authorizationCode', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('avsCode', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('avsCodeRaw', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('cvCode', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('authorizedDateTime', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('processorResponse', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('reconciliationID', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('error_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('cybersource', ['CyberTransaction'])


    def backwards(self, orm):
        # Deleting model 'CyberTransaction'
        db.delete_table('cybersource_cybertransaction')


    models = {
        'cybersource.cybertransaction': {
            'Meta': {'object_name': 'CyberTransaction'},
            'accountNumber': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'authorizationCode': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'authorizedDateTime': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avsCode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'avsCodeRaw': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'customerID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cvCode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cvIndicator': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cvNumber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'decision': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'error_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expirationMonth': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'expirationYear': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'grandTotalAmount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'merchantID': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'merchantReferenceCode': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'processorResponse': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'reasonCode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'reconciliationID': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'requestID': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'requestToken': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cybersource']