# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'NewsEntry._content_rendered'
        db.add_column('news_newsentry', '_content_rendered', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Changing field 'NewsEntry.content'
        db.alter_column('news_newsentry', 'content', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))


    def backwards(self, orm):
        
        # Deleting field 'NewsEntry._content_rendered'
        db.delete_column('news_newsentry', '_content_rendered')

        # Changing field 'NewsEntry.content'
        db.alter_column('news_newsentry', 'content', self.gf('django.db.models.fields.TextField')())


    models = {
        'news.newsentry': {
            'Meta': {'ordering': "['-creation_date']", 'object_name': 'NewsEntry'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {}),
            'content': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']
