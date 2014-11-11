# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialLinks'
        db.create_table(u'socialmedias_sociallinks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True)),
            ('image_mob', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=300, null=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('targt', self.gf('django.db.models.fields.CharField')(default='_blank', max_length=20)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'socialmedias', ['SocialLinks'])


    def backwards(self, orm):
        # Deleting model 'SocialLinks'
        db.delete_table(u'socialmedias_sociallinks')


    models = {
        u'socialmedias.sociallinks': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'SocialLinks'},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True'}),
            'image_mob': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300', 'null': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'targt': ('django.db.models.fields.CharField', [], {'default': "'_blank'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'})
        }
    }

    complete_apps = ['socialmedias']