from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

# south introspection rules 
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^django\.contrib\.gis\.db\.models\.fields\.MultiPolygonField'])
except ImportError:
    pass

# Project choices
PROJECT_STATUS = (
	('con', 'Continuing'),
	('com', 'Completed'),
	('new', 'New'),
	('imp', 'Implementation'),
	('inp', 'In Progress'),
)

MUNICIPALITY_TYPE = (
	('m', 'Multiple'),
	('s', 'Single'),
	('r', 'Regional'),
)

class Project(models.Model):
	"""
	MetroFuture projects; core class for map
	"""
	name = models.CharField(max_length=250)
	lead_dept = models.ForeignKey('Department', related_name='lead')
	collab_dept = models.ManyToManyField('Department', related_name='collab', blank=True, null=True)
	collab_ext = models.CharField('External Collaborator', max_length=50, blank=True, null=True)
	client = models.CharField(max_length=100, blank=True, null=True)
	funding = models.ForeignKey('Funding', blank=True, null=True)
	timing = models.CharField(max_length=50, blank=True, null=True)
	status = models.CharField(max_length=3, choices=PROJECT_STATUS)
	municipalities = models.ManyToManyField('Municipality', blank=True, null=True)
	municipalities_type = models.CharField(max_length=1, choices=MUNICIPALITY_TYPE)
	municipal_specific = models.BooleanField(help_text='Counted as a project in a specific municipality')
	equity = models.BooleanField('Equity related')

	community_types = models.ManyToManyField('CommunityType', blank=True, null=True)
	subregions = models.ManyToManyField('Subregion', blank=True, null=True)	
	strategies = models.ManyToManyField('Strategy', blank=True, null=True)
	goals = models.ManyToManyField('Goal', blank=True, null=True)
	supergoals = models.ManyToManyField('Supergoal', blank=True, null=True)

	active = models.BooleanField('Map candidate')

	# TODO: cache centroid of unionend municipalities

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Department(models.Model):
	"""
	MAPC Departments or Divisions. Only one hierarchy used for simplicity reasons.
	"""
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Funding(models.Model):
	"""
	Funding sources
	"""
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Municipality(models.Model):
	""" Municipalities """
	muni_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	geometry = models.MultiPolygonField(srid=26986)
	objects = models.GeoManager()
    
	def __unicode__(self):
		return self.name
    
	class Meta:
		verbose_name = _('Municipality')
		verbose_name_plural = _('Municipalities')
		ordering = ['name']

class CommunityType(models.Model):
	abbr = models.CharField(max_length=10)
	name = models.CharField(max_length=50, blank=True, null=True)

	def __unicode__(self):
		return self.abbr

class Subregion(models.Model):
	abbr = models.CharField(max_length=10)
	name = models.CharField(max_length=50, blank=True, null=True)

	def __unicode__(self):
		return self.abbr

class Strategy(models.Model):
	"""
	MetroFuture Strategies
	"""
	nr = models.CharField(max_length=5)
	title = models.CharField(max_length=100, blank=True, null=True)

	class Meta:
		verbose_name = _('Strategy')
		verbose_name_plural = _('Strategies')

	def __unicode__(self):
		return self.nr
    
class Goal(models.Model):
	"""
	MetroFuture Goals
	"""
	nr = models.CharField(max_length=5)
	title = models.CharField(max_length=100, blank=True, null=True)
		
	class Meta:
		verbose_name = _('Goal')
		verbose_name_plural = _('Goals')

	def __unicode__(self):
		return self.nr

class Supergoal(models.Model):
	"""
	MetroFuture Supergoals
	"""
	abbr = models.CharField(max_length=2)
	title = models.CharField(max_length=100, blank=True, null=True)

	class Meta:
		verbose_name = _('Supergoal')
		verbose_name_plural = _('Supergoals')

	def __unicode__(self):
		return self.title
    
    
    