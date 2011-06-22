# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Service'
        db.create_table('board_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('board', ['Service'])

        # Adding model 'Status'
        db.create_table('board_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('severity', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('board', ['Status'])

        # Adding model 'Event'
        db.create_table('board_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['board.Service'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['board.Status'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('informational', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('board', ['Event'])


    def backwards(self, orm):
        
        # Deleting model 'Service'
        db.delete_table('board_service')

        # Deleting model 'Status'
        db.delete_table('board_status')

        # Deleting model 'Event'
        db.delete_table('board_event')


    models = {
        'board.event': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informational': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['board.Service']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['board.Status']"})
        },
        'board.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'board.status': {
            'Meta': {'object_name': 'Status'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'severity': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['board']
