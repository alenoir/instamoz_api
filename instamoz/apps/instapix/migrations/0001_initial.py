# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'instapix_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Tag'])

        # Adding model 'Subscription'
        db.create_table(u'instapix_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subscription_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=22)),
            ('location_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('location_lng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['instapix.Tag'], null=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Subscription'])

        # Adding model 'Mosaic'
        db.create_table(u'instapix_mosaic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('location_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('location_lng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pixel_size', self.gf('django.db.models.fields.IntegerField')()),
            ('is_parse', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Mosaic'])

        # Adding M2M table for field tags on 'Mosaic'
        m2m_table_name = db.shorten_name(u'instapix_mosaic_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mosaic', models.ForeignKey(orm[u'instapix.mosaic'], null=False)),
            ('tag', models.ForeignKey(orm[u'instapix.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mosaic_id', 'tag_id'])

        # Adding M2M table for field subscriptions on 'Mosaic'
        m2m_table_name = db.shorten_name(u'instapix_mosaic_subscriptions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mosaic', models.ForeignKey(orm[u'instapix.mosaic'], null=False)),
            ('subscription', models.ForeignKey(orm[u'instapix.subscription'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mosaic_id', 'subscription_id'])

        # Adding model 'InstaPic'
        db.create_table(u'instapix_instapic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.TextField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(max_length=100, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('user_profile_picture', self.gf('django.db.models.fields.TextField')()),
            ('picture_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('picture_url_low', self.gf('django.db.models.fields.TextField')()),
            ('picture_url_high', self.gf('django.db.models.fields.TextField')()),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True)),
            ('r_color', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
            ('g_color', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
            ('b_color', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
            ('location_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('location_lng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('location_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('is_parse', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'instapix', ['InstaPic'])

        # Adding M2M table for field subscriptions on 'InstaPic'
        m2m_table_name = db.shorten_name(u'instapix_instapic_subscriptions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('instapic', models.ForeignKey(orm[u'instapix.instapic'], null=False)),
            ('subscription', models.ForeignKey(orm[u'instapix.subscription'], null=False))
        ))
        db.create_unique(m2m_table_name, ['instapic_id', 'subscription_id'])

        # Adding model 'Pixel'
        db.create_table(u'instapix_pixel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True)),
            ('r_color', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
            ('g_color', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
            ('b_color', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')(default='', blank=True)),
            ('y', self.gf('django.db.models.fields.IntegerField')(default='', blank=True)),
            ('mosaic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pixels', to=orm['instapix.Mosaic'])),
            ('pic', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pixels', null=True, on_delete=models.SET_NULL, to=orm['instapix.InstaPic'])),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'instapix', ['Pixel'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'instapix_tag')

        # Deleting model 'Subscription'
        db.delete_table(u'instapix_subscription')

        # Deleting model 'Mosaic'
        db.delete_table(u'instapix_mosaic')

        # Removing M2M table for field tags on 'Mosaic'
        db.delete_table(db.shorten_name(u'instapix_mosaic_tags'))

        # Removing M2M table for field subscriptions on 'Mosaic'
        db.delete_table(db.shorten_name(u'instapix_mosaic_subscriptions'))

        # Deleting model 'InstaPic'
        db.delete_table(u'instapix_instapic')

        # Removing M2M table for field subscriptions on 'InstaPic'
        db.delete_table(db.shorten_name(u'instapix_instapic_subscriptions'))

        # Deleting model 'Pixel'
        db.delete_table(u'instapix_pixel')


    models = {
        u'instapix.instapic': {
            'Meta': {'object_name': 'InstaPic'},
            'b_color': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'g_color': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_parse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'link': ('django.db.models.fields.TextField', [], {}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picture_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'picture_url_high': ('django.db.models.fields.TextField', [], {}),
            'picture_url_low': ('django.db.models.fields.TextField', [], {}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'r_color': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'subscriptions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'instapics'", 'symmetrical': 'False', 'to': u"orm['instapix.Subscription']"}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user_profile_picture': ('django.db.models.fields.TextField', [], {})
        },
        u'instapix.mosaic': {
            'Meta': {'object_name': 'Mosaic'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_parse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pixel_size': ('django.db.models.fields.IntegerField', [], {}),
            'subscriptions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mosaics'", 'symmetrical': 'False', 'to': u"orm['instapix.Subscription']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['instapix.Tag']", 'symmetrical': 'False'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'instapix.pixel': {
            'Meta': {'object_name': 'Pixel'},
            'b_color': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'g_color': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mosaic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pixels'", 'to': u"orm['instapix.Mosaic']"}),
            'pic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pixels'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['instapix.InstaPic']"}),
            'r_color': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
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