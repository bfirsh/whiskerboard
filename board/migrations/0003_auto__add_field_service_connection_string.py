# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Service.connection_string'
        db.add_column('board_service', 'connection_string', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Service.connection_string'
        db.delete_column('board_service', 'connection_string')


    models = {
        'board.event': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informational': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['board.Service']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['board.Status']"})
        },
        'board.service': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Service'},
            'connection_string': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'board.status': {
            'Meta': {'ordering': "('severity',)", 'object_name': 'Status'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'severity': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['board']
