# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Mosaic.image'
        db.alter_column(u'instapix_mosaic', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Mosaic.image'
        db.alter_column(u'instapix_mosaic', 'image', self.gf('stdimage.fields.StdImageField')(max_length=100, thumbnail_size={'width': 100, 'name': 'thumbnail_size', 'resample': None, 'crop': True, 'height': 100}, size={'width': 620, 'name': 'size', 'resample': None, 'crop': True, 'height': 620}))

    models = {
        u'instapix.instapic': {
            'Meta': {'object_name': 'InstaPic'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picture_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'picture_url_high': ('django.db.models.fields.TextField', [], {}),
            'picture_url_low': ('django.db.models.fields.TextField', [], {}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user_profile_picture': ('django.db.models.fields.TextField', [], {})
        },
        u'instapix.mosaic': {
            'Meta': {'object_name': 'Mosaic'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_parse': ('django.db.models.fields.BooleanField', [], {}),
            'location_lat': ('django.db.models.fields.FloatField', [], {}),
            'location_lng': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subscriptions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mosaics'", 'symmetrical': 'False', 'to': u"orm['instapix.Subscription']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['instapix.Tag']", 'symmetrical': 'False'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'instapix.pixel': {
            'Meta': {'object_name': 'Pixel'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mosaic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pixels'", 'to': u"orm['instapix.Mosaic']"}),
            'pic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pixels'", 'null': 'True', 'to': u"orm['instapix.InstaPic']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': "''", 'blank': 'True'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': "''", 'blank': 'True'})
        },
        u'instapix.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subscription_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['instapix.Tag']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '22'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'instapix.tag': {
            'Meta': {'object_name': 'Tag'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['instapix']