# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SocialLinks.image_mob'
        db.delete_column(u'socialmedias_sociallinks', 'image_mob')


    def backwards(self, orm):
        # Adding field 'SocialLinks.image_mob'
        db.add_column(u'socialmedias_sociallinks', 'image_mob',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    models = {
        u'socialmedias.sociallinks': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'SocialLinks'},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300', 'null': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'targt': ('django.db.models.fields.CharField', [], {'default': "'_blank'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'})
        }
    }

    complete_apps = ['socialmedias']