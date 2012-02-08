# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('iamap_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('lead_dept', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lead', to=orm['iamap.Department'])),
            ('collab_ext', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('funding', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iamap.Funding'], null=True, blank=True)),
            ('timing', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('municipalities_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('municipal_specific', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('equity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('iamap', ['Project'])

        # Adding M2M table for field collab_dept on 'Project'
        db.create_table('iamap_project_collab_dept', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['iamap.project'], null=False)),
            ('department', models.ForeignKey(orm['iamap.department'], null=False))
        ))
        db.create_unique('iamap_project_collab_dept', ['project_id', 'department_id'])

        # Adding M2M table for field municipalities on 'Project'
        db.create_table('iamap_project_municipalities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['iamap.project'], null=False)),
            ('municipality', models.ForeignKey(orm['iamap.municipality'], null=False))
        ))
        db.create_unique('iamap_project_municipalities', ['project_id', 'municipality_id'])

        # Adding M2M table for field community_types on 'Project'
        db.create_table('iamap_project_community_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['iamap.project'], null=False)),
            ('communitytype', models.ForeignKey(orm['iamap.communitytype'], null=False))
        ))
        db.create_unique('iamap_project_community_types', ['project_id', 'communitytype_id'])

        # Adding M2M table for field subregions on 'Project'
        db.create_table('iamap_project_subregions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['iamap.project'], null=False)),
            ('subregion', models.ForeignKey(orm['iamap.subregion'], null=False))
        ))
        db.create_unique('iamap_project_subregions', ['project_id', 'subregion_id'])

        # Adding M2M table for field strategies on 'Project'
        db.create_table('iamap_project_strategies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['iamap.project'], null=False)),
            ('strategy', models.ForeignKey(orm['iamap.strategy'], null=False))
        ))
        db.create_unique('iamap_project_strategies', ['project_id', 'strategy_id'])

        # Adding M2M table for field goals on 'Project'
        db.create_table('iamap_project_goals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['iamap.project'], null=False)),
            ('goal', models.ForeignKey(orm['iamap.goal'], null=False))
        ))
        db.create_unique('iamap_project_goals', ['project_id', 'goal_id'])

        # Adding M2M table for field supergoals on 'Project'
        db.create_table('iamap_project_supergoals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['iamap.project'], null=False)),
            ('supergoal', models.ForeignKey(orm['iamap.supergoal'], null=False))
        ))
        db.create_unique('iamap_project_supergoals', ['project_id', 'supergoal_id'])

        # Adding model 'Department'
        db.create_table('iamap_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('iamap', ['Department'])

        # Adding model 'Funding'
        db.create_table('iamap_funding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('iamap', ['Funding'])

        # Adding model 'Municipality'
        db.create_table('iamap_municipality', (
            ('muni_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('iamap', ['Municipality'])

        # Adding model 'CommunityType'
        db.create_table('iamap_communitytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('iamap', ['CommunityType'])

        # Adding model 'Subregion'
        db.create_table('iamap_subregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('iamap', ['Subregion'])

        # Adding model 'Strategy'
        db.create_table('iamap_strategy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('iamap', ['Strategy'])

        # Adding model 'Goal'
        db.create_table('iamap_goal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('iamap', ['Goal'])

        # Adding model 'Supergoal'
        db.create_table('iamap_supergoal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('iamap', ['Supergoal'])


    def backwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('iamap_project')

        # Removing M2M table for field collab_dept on 'Project'
        db.delete_table('iamap_project_collab_dept')

        # Removing M2M table for field municipalities on 'Project'
        db.delete_table('iamap_project_municipalities')

        # Removing M2M table for field community_types on 'Project'
        db.delete_table('iamap_project_community_types')

        # Removing M2M table for field subregions on 'Project'
        db.delete_table('iamap_project_subregions')

        # Removing M2M table for field strategies on 'Project'
        db.delete_table('iamap_project_strategies')

        # Removing M2M table for field goals on 'Project'
        db.delete_table('iamap_project_goals')

        # Removing M2M table for field supergoals on 'Project'
        db.delete_table('iamap_project_supergoals')

        # Deleting model 'Department'
        db.delete_table('iamap_department')

        # Deleting model 'Funding'
        db.delete_table('iamap_funding')

        # Deleting model 'Municipality'
        db.delete_table('iamap_municipality')

        # Deleting model 'CommunityType'
        db.delete_table('iamap_communitytype')

        # Deleting model 'Subregion'
        db.delete_table('iamap_subregion')

        # Deleting model 'Strategy'
        db.delete_table('iamap_strategy')

        # Deleting model 'Goal'
        db.delete_table('iamap_goal')

        # Deleting model 'Supergoal'
        db.delete_table('iamap_supergoal')


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
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
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
