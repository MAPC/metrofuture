# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.municipal_specific'
        db.delete_column(u'projects_project', 'municipal_specific')

        # Adding field 'Project.start_date'
        db.add_column(u'projects_project', 'start_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2000, 1, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Project.end_date'
        db.add_column(u'projects_project', 'end_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.subregions_string'
        db.add_column(u'projects_project', 'subregions_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Project.lead_dept_string'
        db.add_column(u'projects_project', 'lead_dept_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Project.community_type_string'
        db.add_column(u'projects_project', 'community_type_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Project.nr_subgoals'
        db.add_column(u'projects_project', 'nr_subgoals',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Project.nr_goals'
        db.add_column(u'projects_project', 'nr_goals',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Project.nr_municipalities'
        db.add_column(u'projects_project', 'nr_municipalities',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Removing M2M table for field community_types on 'Project'
        db.delete_table('projects_project_community_types')


    def backwards(self, orm):
        # Adding field 'Project.municipal_specific'
        db.add_column(u'projects_project', 'municipal_specific',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Project.start_date'
        db.delete_column(u'projects_project', 'start_date')

        # Deleting field 'Project.end_date'
        db.delete_column(u'projects_project', 'end_date')

        # Deleting field 'Project.subregions_string'
        db.delete_column(u'projects_project', 'subregions_string')

        # Deleting field 'Project.lead_dept_string'
        db.delete_column(u'projects_project', 'lead_dept_string')

        # Deleting field 'Project.community_type_string'
        db.delete_column(u'projects_project', 'community_type_string')

        # Deleting field 'Project.nr_subgoals'
        db.delete_column(u'projects_project', 'nr_subgoals')

        # Deleting field 'Project.nr_goals'
        db.delete_column(u'projects_project', 'nr_goals')

        # Deleting field 'Project.nr_municipalities'
        db.delete_column(u'projects_project', 'nr_municipalities')

        # Adding M2M table for field community_types on 'Project'
        db.create_table(u'projects_project_community_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('communitytype', models.ForeignKey(orm[u'projects.communitytype'], null=False))
        ))
        db.create_unique(u'projects_project_community_types', ['project_id', 'communitytype_id'])


    models = {
        u'projects.communitytype': {
            'Meta': {'object_name': 'CommunityType'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'projects.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'projects.funding': {
            'Meta': {'object_name': 'Funding'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'projects.goal': {
            'Meta': {'ordering': "['id']", 'object_name': 'Goal'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'projects.municipality': {
            'Meta': {'ordering': "['name']", 'object_name': 'Municipality'},
            'community_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.CommunityType']", 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'muni_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subregion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Subregion']", 'null': 'True', 'blank': 'True'})
        },
        u'projects.project': {
            'Meta': {'ordering': "['name']", 'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'collab_dept': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'collab'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['projects.Department']"}),
            'collab_ext': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'community_type_string': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'equity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'equity_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'funding': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Funding']", 'null': 'True', 'blank': 'True'}),
            'goals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Goal']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lead_dept': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lead'", 'symmetrical': 'False', 'to': u"orm['projects.Department']"}),
            'lead_dept_string': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'municipalities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['projects.Municipality']"}),
            'municipalities_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nr_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nr_municipalities': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nr_subgoals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '3'}),
            'strategies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Strategy']", 'null': 'True', 'blank': 'True'}),
            'subgoals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.SubGoal']", 'null': 'True', 'blank': 'True'}),
            'subregions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Subregion']", 'null': 'True', 'blank': 'True'}),
            'subregions_string': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'substrategies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.SubStrategy']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'timing': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'projects.strategy': {
            'Meta': {'ordering': "['nr']", 'object_name': 'Strategy'},
            'nr': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'projects.subgoal': {
            'Meta': {'ordering': "['nr']", 'object_name': 'SubGoal'},
            'goal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Goal']"}),
            'nr': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'projects.subregion': {
            'Meta': {'ordering': "['name']", 'object_name': 'Subregion'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'projects.substrategy': {
            'Meta': {'ordering': "['strategy', 'letter']", 'unique_together': "(('strategy', 'letter'),)", 'object_name': 'SubStrategy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'strategy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Strategy']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']