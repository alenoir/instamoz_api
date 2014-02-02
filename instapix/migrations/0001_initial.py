# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mosaic'
        db.create_table(u'instapix_mosaic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('tags', self.gf('django.db.models.fields.TextField')()),
            ('geo', self.gf('django.db.models.fields.TextField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Mosaic'])

        # Adding model 'Pixel'
        db.create_table(u'instapix_pixel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')(default='', blank=True)),
            ('y', self.gf('django.db.models.fields.IntegerField')(default='', blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Pixel'])

        # Adding model 'InstaPic'
        db.create_table(u'instapix_instapic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.TextField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(max_length=100, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('picture_id', self.gf('django.db.models.fields.IntegerField')(max_length=100, blank=True)),
            ('picture_url_low', self.gf('django.db.models.fields.TextField')()),
            ('picture_url_high', self.gf('django.db.models.fields.TextField')()),
            ('user_profile_picture', self.gf('django.db.models.fields.TextField')()),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True)),
            ('location_lat', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('location_lng', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('location_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'instapix', ['InstaPic'])


    def backwards(self, orm):
        # Deleting model 'Mosaic'
        db.delete_table(u'instapix_mosaic')

        # Deleting model 'Pixel'
        db.delete_table(u'instapix_pixel')

        # Deleting model 'InstaPic'
        db.delete_table(u'instapix_instapic')


    models = {
        u'instapix.instapic': {
            'Meta': {'object_name': 'InstaPic'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'picture_id': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'blank': 'True'}),
            'picture_url_high': ('django.db.models.fields.TextField', [], {}),
            'picture_url_low': ('django.db.models.fields.TextField', [], {}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user_profile_picture': ('django.db.models.fields.TextField', [], {})
        },
        u'instapix.mosaic': {
            'Meta': {'object_name': 'Mosaic'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'geo': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.TextField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'instapix.pixel': {
            'Meta': {'object_name': 'Pixel'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': "''", 'blank': 'True'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['instapix']