# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactUs'
        db.create_table(u'contact_contactus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('msg', self.gf('django.db.models.fields.TextField')(default=False)),
        ))
        db.send_create_signal(u'contact', ['ContactUs'])


    def backwards(self, orm):
        # Deleting model 'ContactUs'
        db.delete_table(u'contact_contactus')


    models = {
        u'contact.contactus': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContactUs'},
            'contact_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.TextField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['contact']