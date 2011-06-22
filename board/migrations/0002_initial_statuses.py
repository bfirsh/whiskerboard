# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.Status.objects.create(
            name="Down", 
            slug="down", 
            image="cross-circle", 
            severity=40,
            description="The service is currently down"
        )
        orm.Status.objects.create(
            name="Up", 
            slug="up", 
            image="tick-circle", 
            severity=10,
            description="The service is up"
        )
        orm.Status.objects.create(
            name="Warning", 
            slug="warning", 
            image="exclamation", 
            severity=30,
            description="The service is experiencing intermittent problems"
        )



    def backwards(self, orm):
        "Write your backwards methods here."


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
            'Meta': {'ordering': "('name',)", 'object_name': 'Service'},
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
