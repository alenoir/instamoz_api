# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Tags'
        db.delete_table(u'instapix_tags')

        # Adding model 'Tag'
        db.create_table(u'instapix_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Tag'])

        # Deleting field 'Mosaic.tags'
        db.delete_column(u'instapix_mosaic', 'tags_id')

        # Adding M2M table for field tags on 'Mosaic'
        m2m_table_name = db.shorten_name(u'instapix_mosaic_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mosaic', models.ForeignKey(orm[u'instapix.mosaic'], null=False)),
            ('tag', models.ForeignKey(orm[u'instapix.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mosaic_id', 'tag_id'])


    def backwards(self, orm):
        # Adding model 'Tags'
        db.create_table(u'instapix_tags', (
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Tags'])

        # Deleting model 'Tag'
        db.delete_table(u'instapix_tag')

        # Adding field 'Mosaic.tags'
        db.add_column(u'instapix_mosaic', 'tags',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='Mosaics', to=orm['instapix.Tags']),
                      keep_default=False)

        # Removing M2M table for field tags on 'Mosaic'
        db.delete_table(db.shorten_name(u'instapix_mosaic_tags'))


    models = {
        u'instapix.instapic': {
            'Meta': {'object_name': 'InstaPic'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_parse': ('django.db.models.fields.BooleanField', [], {}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
        u'instapix.tag': {
            'Meta': {'object_name': 'Tag'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['instapix']