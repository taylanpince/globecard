# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Location._content_rendered'
        db.add_column('locations_location', '_content_rendered', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Changing field 'Location.content'
        db.alter_column('locations_location', 'content', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))

        # Adding field 'Client._content_rendered'
        db.add_column('locations_client', '_content_rendered', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Changing field 'Client.content'
        db.alter_column('locations_client', 'content', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))


    def backwards(self, orm):
        
        # Deleting field 'Location._content_rendered'
        db.delete_column('locations_location', '_content_rendered')

        # Changing field 'Location.content'
        db.alter_column('locations_location', 'content', self.gf('django.db.models.fields.TextField')())

        # Deleting field 'Client._content_rendered'
        db.delete_column('locations_client', '_content_rendered')

        # Changing field 'Client.content'
        db.alter_column('locations_client', 'content', self.gf('django.db.models.fields.TextField')())


    models = {
        'locations.client': {
            'Meta': {'ordering': "['order']", 'object_name': 'Client'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {}),
            'content': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clients'", 'to': "orm['locations.Location']"}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'locations.location': {
            'Meta': {'ordering': "['order']", 'object_name': 'Location'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {}),
            'content': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['locations']
