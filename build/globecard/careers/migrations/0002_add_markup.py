# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'JobPosition.prerequisites'
        db.delete_column('careers_jobposition', 'prerequisites')

        # Adding field 'JobPosition._description_rendered'
        db.add_column('careers_jobposition', '_description_rendered', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Changing field 'JobPosition.description'
        db.alter_column('careers_jobposition', 'description', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))


    def backwards(self, orm):
        
        # Adding field 'JobPosition.prerequisites'
        db.add_column('careers_jobposition', 'prerequisites', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Deleting field 'JobPosition._description_rendered'
        db.delete_column('careers_jobposition', '_description_rendered')

        # Changing field 'JobPosition.description'
        db.alter_column('careers_jobposition', 'description', self.gf('django.db.models.fields.TextField')())


    models = {
        'careers.jobapplication': {
            'Meta': {'ordering': "['application_date']", 'object_name': 'JobApplication'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'application_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_time': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': "orm['careers.JobPosition']"})
        },
        'careers.jobposition': {
            'Meta': {'ordering': "['order', '-creation_date']", 'object_name': 'JobPosition'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['careers']
