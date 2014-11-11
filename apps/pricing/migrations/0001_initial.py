# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DemoPricing'
        db.create_table(u'pricing_demopricing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'pricing', ['DemoPricing'])

        # Adding model 'Features'
        db.create_table(u'pricing_features', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('demopricing', self.gf('django.db.models.fields.related.ForeignKey')(related_name='demo_features', to=orm['pricing.DemoPricing'])),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pricing', ['Features'])

        # Adding model 'ActiveDemoPricing'
        db.create_table(u'pricing_activedemopricing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('demopricing', self.gf('django.db.models.fields.related.ForeignKey')(related_name='active_demos', to=orm['pricing.DemoPricing'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('mobile_no', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('msg', self.gf('django.db.models.fields.TextField')()),
            ('activated_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 4, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'pricing', ['ActiveDemoPricing'])


    def backwards(self, orm):
        # Deleting model 'DemoPricing'
        db.delete_table(u'pricing_demopricing')

        # Deleting model 'Features'
        db.delete_table(u'pricing_features')

        # Deleting model 'ActiveDemoPricing'
        db.delete_table(u'pricing_activedemopricing')


    models = {
        u'pricing.activedemopricing': {
            'Meta': {'object_name': 'ActiveDemoPricing'},
            'activated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 4, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'demopricing': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'active_demos'", 'to': u"orm['pricing.DemoPricing']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_no': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'msg': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pricing.demopricing': {
            'Meta': {'object_name': 'DemoPricing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'pricing.features': {
            'Meta': {'object_name': 'Features'},
            'demopricing': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demo_features'", 'to': u"orm['pricing.DemoPricing']"}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['pricing']