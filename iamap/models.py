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
)

MUNICIPALITY_TYPE = (
    ('m', 'Multiple'),
    ('s', 'Single'),
    ('r', 'Regional'),
)


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


class CommunityType(models.Model):
    abbr = models.CharField(max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Subregion(models.Model):
    abbr = models.CharField(max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return self.name

    def muni_string(self):
        """ Returns a stringified municipality list. """
        muni_list = [str(muni.pk) for muni in self.municipality_set.filter(projects__active=True).distinct()]
        return ','.join(muni_list)


class Municipality(models.Model):
    """ Municipalities """
    muni_id = models.IntegerField('Muni ID', primary_key=True)
    name = models.CharField(max_length=50)
    community_type = models.ForeignKey(CommunityType, null=True, blank=True)
    subregion = models.ManyToManyField(Subregion, null=True, blank=True)
    geometry = models.MultiPolygonField(geography=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Municipality')
        verbose_name_plural = _('Municipalities')
        ordering = ['name']


class Strategy(models.Model):
    """
    MetroFuture Strategies
    """
    nr = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _('Strategy')
        verbose_name_plural = _('Strategies')
        ordering = ['nr', ]

    def __unicode__(self):
        return '%d. %s' % (self.nr, self.title)

    def substrategies_string(self):
        """ Returns a stringified substrategy list. """
        substrategies_list = [str(substrategy.pk) for substrategy in self.substrategy_set.filter(project__active=True).distinct()]
        return ','.join(substrategies_list)


class SubStrategy(models.Model):
    """
    MetroFuture SubStrategies
    """
    title = models.CharField(max_length=100, blank=True, null=True)
    strategy = models.ForeignKey(Strategy)
    letter = models.CharField(max_length=1)

    class Meta:
        verbose_name = _('Sub-Strategy')
        verbose_name_plural = _('Sub-Strategies')
        ordering = ['strategy', 'letter']
        unique_together = (('strategy', 'letter'),)

    def __unicode__(self):
        return '%d.%s %s' % (self.strategy.nr, self.letter, self.title)

    @property
    def nr(self):
        return '%d.%s' % (self.strategy.nr, self.letter)
    

class Supergoal(models.Model):
    """
    MetroFuture Goals (initially called 'Supergoals')
    """
    abbr = models.CharField(max_length=2)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _('Goal')
        verbose_name_plural = _('Goals')
        ordering = ['id']

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.abbr)

    def goals_string(self):
        """ Returns a stringified substrategy list. """
        goals_list = [str(goal.pk) for goal in self.goal_set.filter(project__active=True).distinct()]
        return ','.join(goals_list)


class Goal(models.Model):
    """
    MetroFuture Subgoals (initially called 'Goals')
    """
    nr = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    supergoal = models.ForeignKey(Supergoal)
        
    class Meta:
        verbose_name = _('Subgoal')
        verbose_name_plural = _('Subgoals')
        ordering = ['nr']

    def __unicode__(self):
        return '%d (%s) %s' % (self.nr, self.supergoal.abbr, self.title)


class Project(models.Model):
    """
    MetroFuture projects; core class for map
    """
    name = models.CharField(max_length=250)
    desc = models.TextField('Short description', blank=True, null=True)
    url = models.URLField('Project URL', blank=True, null=True)
    thumbnail = models.ImageField('Project picture', help_text='Image dimensions should be 160x120', upload_to='project_tn', blank=True, null=True)
    lead_dept = models.ManyToManyField(Department, related_name='lead', verbose_name=u'Lead Departments')
    collab_dept = models.ManyToManyField(Department, related_name='collab', blank=True, null=True)
    collab_ext = models.CharField('External Collaborator', max_length=50, blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    funding = models.ForeignKey('Funding', blank=True, null=True)
    timing = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=3, choices=PROJECT_STATUS)
    municipalities = models.ManyToManyField(Municipality, blank=True, null=True, related_name='projects')
    municipalities_type = models.CharField(max_length=1, choices=MUNICIPALITY_TYPE)
    municipal_specific = models.BooleanField(help_text='Counted as a project in a specific municipality')

    equity = models.BooleanField('Equity related')
    equity_comment = models.TextField(null=True, blank=True)

    # FIXME: redundant moved to municipality
    community_types = models.ManyToManyField(CommunityType, blank=True, null=True)
    subregions = models.ManyToManyField(Subregion, blank=True, null=True)   

    # FIXME: redundant, field required by client
    strategies = models.ManyToManyField(Strategy, blank=True, null=True)
    substrategies = models.ManyToManyField(SubStrategy, blank=True, null=True)
    goals = models.ManyToManyField(Goal, blank=True, null=True, verbose_name=u'Subgoals')
    # FIXME: redundant, field required by client
    supergoals = models.ManyToManyField(Supergoal, blank=True, null=True, verbose_name=u'Goals')

    active = models.BooleanField('Shown on map')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']   

    # TODO: m2m_changed signal to add supergoals from goals and strategies from substrategies     

        


    
    