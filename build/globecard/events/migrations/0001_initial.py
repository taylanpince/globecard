# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EventCategory'
        db.create_table('events_eventcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('events', ['EventCategory'])

        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['events.EventCategory'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('dates', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('events', ['Event'])


    def backwards(self, orm):
        
        # Deleting model 'EventCategory'
        db.delete_table('events_eventcategory')

        # Deleting model 'Event'
        db.delete_table('events_event')


    models = {
        'events.event': {
            'Meta': {'ordering': "['order']", 'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['events.EventCategory']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dates': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'events.eventcategory': {
            'Meta': {'ordering': "['order']", 'object_name': 'EventCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['events']
