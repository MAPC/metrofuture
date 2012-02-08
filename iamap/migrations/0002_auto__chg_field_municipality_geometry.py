# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Municipality.geometry'
        db.alter_column('iamap_municipality', 'geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=3857))


    def backwards(self, orm):
        
        # Changing field 'Municipality.geometry'
        db.alter_column('iamap_municipality', 'geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')())


    models = {
        'iamap.communitytype': {
            'Meta': {'object_name': 'CommunityType'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'iamap.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'iamap.funding': {
            'Meta': {'object_name': 'Funding'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'iamap.goal': {
            'Meta': {'object_name': 'Goal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'iamap.municipality': {
            'Meta': {'ordering': "['name']", 'object_name': 'Municipality'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857'}),
            'muni_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'iamap.project': {
            'Meta': {'ordering': "['name']", 'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'collab_dept': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'collab'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['iamap.Department']"}),
            'collab_ext': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'community_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['iamap.CommunityType']", 'null': 'True', 'blank': 'True'}),
            'equity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'funding': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iamap.Funding']", 'null': 'True', 'blank': 'True'}),
            'goals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['iamap.Goal']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_dept': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lead'", 'to': "orm['iamap.Department']"}),
            'municipal_specific': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'municipalities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['iamap.Municipality']", 'null': 'True', 'blank': 'True'}),
            'municipalities_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'strategies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['iamap.Strategy']", 'null': 'True', 'blank': 'True'}),
            'subregions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['iamap.Subregion']", 'null': 'True', 'blank': 'True'}),
            'supergoals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['iamap.Supergoal']", 'null': 'True', 'blank': 'True'}),
            'timing': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'iamap.strategy': {
            'Meta': {'object_name': 'Strategy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'iamap.subregion': {
            'Meta': {'object_name': 'Subregion'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'iamap.supergoal': {
            'Meta': {'object_name': 'Supergoal'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['iamap']
