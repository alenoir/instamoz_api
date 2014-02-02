# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Mosaic.geo'
        db.delete_column(u'instapix_mosaic', 'geo')

        # Adding field 'Mosaic.location_lat'
        db.add_column(u'instapix_mosaic', 'location_lat',
                      self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True),
                      keep_default=False)

        # Adding field 'Mosaic.location_lng'
        db.add_column(u'instapix_mosaic', 'location_lng',
                      self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Mosaic.geo'
        db.add_column(u'instapix_mosaic', 'geo',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Mosaic.location_lat'
        db.delete_column(u'instapix_mosaic', 'location_lat')

        # Deleting field 'Mosaic.location_lng'
        db.delete_column(u'instapix_mosaic', 'location_lng')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
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