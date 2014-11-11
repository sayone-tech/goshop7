# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ContactUs.user_ip'
        db.add_column(u'contact_contactus', 'user_ip',
                      self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ContactUs.country'
        db.add_column(u'contact_contactus', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ContactUs.city'
        db.add_column(u'contact_contactus', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ContactUs.browser_information'
        db.add_column(u'contact_contactus', 'browser_information',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ContactUs.user_ip'
        db.delete_column(u'contact_contactus', 'user_ip')

        # Deleting field 'ContactUs.country'
        db.delete_column(u'contact_contactus', 'country')

        # Deleting field 'ContactUs.city'
        db.delete_column(u'contact_contactus', 'city')

        # Deleting field 'ContactUs.browser_information'
        db.delete_column(u'contact_contactus', 'browser_information')


    models = {
        u'contact.contactus': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContactUs'},
            'browser_information': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 4, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.TextField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contact']