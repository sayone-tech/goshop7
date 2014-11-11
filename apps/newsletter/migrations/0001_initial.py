# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsletterSubscription'
        db.create_table(u'newsletter_newslettersubscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('hash_key', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('confirm', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'newsletter', ['NewsletterSubscription'])

        # Adding model 'Newsletter'
        db.create_table(u'newsletter_newsletter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('message', self.gf('ckeditor.fields.RichTextField')()),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('send', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'newsletter', ['Newsletter'])


    def backwards(self, orm):
        # Deleting model 'NewsletterSubscription'
        db.delete_table(u'newsletter_newslettersubscription')

        # Deleting model 'Newsletter'
        db.delete_table(u'newsletter_newsletter')


    models = {
        u'newsletter.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('ckeditor.fields.RichTextField', [], {}),
            'send': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'newsletter.newslettersubscription': {
            'Meta': {'ordering': "('email',)", 'object_name': 'NewsletterSubscription'},
            'confirm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'hash_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['newsletter']