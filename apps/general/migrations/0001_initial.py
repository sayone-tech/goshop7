# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeneralSettings'
        db.create_table(u'general_generalsettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(related_name='site_settings', unique=True, to=orm['sites.Site'])),
            ('start', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('end', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('now', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'general', ['GeneralSettings'])


    def backwards(self, orm):
        # Deleting model 'GeneralSettings'
        db.delete_table(u'general_generalsettings')


    models = {
        u'general.generalsettings': {
            'Meta': {'object_name': 'GeneralSettings'},
            'end': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'now': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'site_settings'", 'unique': 'True', 'to': u"orm['sites.Site']"}),
            'start': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['general']