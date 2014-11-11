# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DemoPricing.discount_price'
        db.add_column(u'pricing_demopricing', 'discount_price',
                      self.gf('django.db.models.fields.DecimalField')(default=900, max_digits=8, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DemoPricing.discount_price'
        db.delete_column(u'pricing_demopricing', 'discount_price')


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
            'discount_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
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