# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'projects_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'projects', ['Department'])

        # Adding model 'Funding'
        db.create_table(u'projects_funding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'projects', ['Funding'])

        # Adding model 'CommunityType'
        db.create_table(u'projects_communitytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['CommunityType'])

        # Adding model 'Subregion'
        db.create_table(u'projects_subregion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Subregion'])

        # Adding model 'Municipality'
        db.create_table(u'projects_municipality', (
            ('muni_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('community_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.CommunityType'], null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'projects', ['Municipality'])

        # Adding M2M table for field subregion on 'Municipality'
        db.create_table(u'projects_municipality_subregion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('municipality', models.ForeignKey(orm[u'projects.municipality'], null=False)),
            ('subregion', models.ForeignKey(orm[u'projects.subregion'], null=False))
        ))
        db.create_unique(u'projects_municipality_subregion', ['municipality_id', 'subregion_id'])

        # Adding model 'Strategy'
        db.create_table(u'projects_strategy', (
            ('nr', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Strategy'])

        # Adding model 'SubStrategy'
        db.create_table(u'projects_substrategy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('strategy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Strategy'])),
            ('letter', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'projects', ['SubStrategy'])

        # Adding unique constraint on 'SubStrategy', fields ['strategy', 'letter']
        db.create_unique(u'projects_substrategy', ['strategy_id', 'letter'])

        # Adding model 'Goal'
        db.create_table(u'projects_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Goal'])

        # Adding model 'SubGoal'
        db.create_table(u'projects_subgoal', (
            ('nr', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('goal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Goal'])),
        ))
        db.send_create_signal(u'projects', ['SubGoal'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('collab_ext', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('funding', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Funding'], null=True, blank=True)),
            ('timing', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('municipalities_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('municipal_specific', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('equity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('equity_comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding M2M table for field lead_dept on 'Project'
        db.create_table(u'projects_project_lead_dept', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('department', models.ForeignKey(orm[u'projects.department'], null=False))
        ))
        db.create_unique(u'projects_project_lead_dept', ['project_id', 'department_id'])

        # Adding M2M table for field collab_dept on 'Project'
        db.create_table(u'projects_project_collab_dept', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('department', models.ForeignKey(orm[u'projects.department'], null=False))
        ))
        db.create_unique(u'projects_project_collab_dept', ['project_id', 'department_id'])

        # Adding M2M table for field municipalities on 'Project'
        db.create_table(u'projects_project_municipalities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('municipality', models.ForeignKey(orm[u'projects.municipality'], null=False))
        ))
        db.create_unique(u'projects_project_municipalities', ['project_id', 'municipality_id'])

        # Adding M2M table for field community_types on 'Project'
        db.create_table(u'projects_project_community_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('communitytype', models.ForeignKey(orm[u'projects.communitytype'], null=False))
        ))
        db.create_unique(u'projects_project_community_types', ['project_id', 'communitytype_id'])

        # Adding M2M table for field subregions on 'Project'
        db.create_table(u'projects_project_subregions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('subregion', models.ForeignKey(orm[u'projects.subregion'], null=False))
        ))
        db.create_unique(u'projects_project_subregions', ['project_id', 'subregion_id'])

        # Adding M2M table for field strategies on 'Project'
        db.create_table(u'projects_project_strategies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('strategy', models.ForeignKey(orm[u'projects.strategy'], null=False))
        ))
        db.create_unique(u'projects_project_strategies', ['project_id', 'strategy_id'])

        # Adding M2M table for field substrategies on 'Project'
        db.create_table(u'projects_project_substrategies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('substrategy', models.ForeignKey(orm[u'projects.substrategy'], null=False))
        ))
        db.create_unique(u'projects_project_substrategies', ['project_id', 'substrategy_id'])

        # Adding M2M table for field subgoals on 'Project'
        db.create_table(u'projects_project_subgoals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('subgoal', models.ForeignKey(orm[u'projects.subgoal'], null=False))
        ))
        db.create_unique(u'projects_project_subgoals', ['project_id', 'subgoal_id'])

        # Adding M2M table for field goals on 'Project'
        db.create_table(u'projects_project_goals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('goal', models.ForeignKey(orm[u'projects.goal'], null=False))
        ))
        db.create_unique(u'projects_project_goals', ['project_id', 'goal_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SubStrategy', fields ['strategy', 'letter']
        db.delete_unique(u'projects_substrategy', ['strategy_id', 'letter'])

        # Deleting model 'Department'
        db.delete_table(u'projects_department')

        # Deleting model 'Funding'
        db.delete_table(u'projects_funding')

        # Deleting model 'CommunityType'
        db.delete_table(u'projects_communitytype')

        # Deleting model 'Subregion'
        db.delete_table(u'projects_subregion')

        # Deleting model 'Municipality'
        db.delete_table(u'projects_municipality')

        # Removing M2M table for field subregion on 'Municipality'
        db.delete_table('projects_municipality_subregion')

        # Deleting model 'Strategy'
        db.delete_table(u'projects_strategy')

        # Deleting model 'SubStrategy'
        db.delete_table(u'projects_substrategy')

        # Deleting model 'Goal'
        db.delete_table(u'projects_goal')

        # Deleting model 'SubGoal'
        db.delete_table(u'projects_subgoal')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Removing M2M table for field lead_dept on 'Project'
        db.delete_table('projects_project_lead_dept')

        # Removing M2M table for field collab_dept on 'Project'
        db.delete_table('projects_project_collab_dept')

        # Removing M2M table for field municipalities on 'Project'
        db.delete_table('projects_project_municipalities')

        # Removing M2M table for field community_types on 'Project'
        db.delete_table('projects_project_community_types')

        # Removing M2M table for field subregions on 'Project'
        db.delete_table('projects_project_subregions')

        # Removing M2M table for field strategies on 'Project'
        db.delete_table('projects_project_strategies')

        # Removing M2M table for field substrategies on 'Project'
        db.delete_table('projects_project_substrategies')

        # Removing M2M table for field subgoals on 'Project'
        db.delete_table('projects_project_subgoals')

        # Removing M2M table for field goals on 'Project'
        db.delete_table('projects_project_goals')


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
            'community_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.CommunityType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'equity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'equity_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'funding': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Funding']", 'null': 'True', 'blank': 'True'}),
            'goals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Goal']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lead_dept': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lead'", 'symmetrical': 'False', 'to': u"orm['projects.Department']"}),
            'municipal_specific': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'municipalities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['projects.Municipality']"}),
            'municipalities_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'strategies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Strategy']", 'null': 'True', 'blank': 'True'}),
            'subgoals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.SubGoal']", 'null': 'True', 'blank': 'True'}),
            'subregions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Subregion']", 'null': 'True', 'blank': 'True'}),
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