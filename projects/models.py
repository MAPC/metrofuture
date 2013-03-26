from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

# south introspection rules 
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^django\.contrib\.gis\.db\.models\.fields\.MultiPolygonField'])
except ImportError:
    pass


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
    

class Goal(models.Model): # Goal
    """
    MetroFuture Goals
    """
    abbr = models.CharField(max_length=2)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _('Goal')
        verbose_name_plural = _('Goals')
        ordering = ['id']

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.abbr)

    def subgoals_string(self):
        """ Returns a stringified substrategy list. """
        subgoals_list = [str(goal.pk) for goal in self.subgoal_set.filter(project__active=True).distinct()]
        return ','.join(subgoals_list)


class SubGoal(models.Model): #SubGoal
    """
    MetroFuture Subgoals
    """
    nr = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    goal = models.ForeignKey(Goal)
        
    class Meta:
        verbose_name = _('Subgoal')
        verbose_name_plural = _('Subgoals')
        ordering = ['nr']

    def __unicode__(self):
        return '%d (%s) %s' % (self.nr, self.goal.abbr, self.title)


class Project(models.Model):
    """
    MetroFuture projects; core class for map
    """

    # Project choices
    PROJECT_STATUS = (
        ('con', 'Continuing'),
        ('com', 'Completed'),
        ('new', 'New'),
    )

    MUNICIPALITY_TYPE = (
        ('m', 'Multiple'),
        ('s', 'Single'),
        ('r', 'Region-wide'),
        ('i', 'Internally Focused'),
    )

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
    status = models.CharField(max_length=3, choices=PROJECT_STATUS, default='new')
    municipalities = models.ManyToManyField(Municipality, blank=True, null=True, related_name='projects')
    municipalities_type = models.CharField(max_length=1, choices=MUNICIPALITY_TYPE)
    subregions = models.ManyToManyField(Subregion, blank=True, null=True) 

    # INFO: dependencies resolved with JavaScript in form
    # TODO: add dependency condition to form clean method
    strategies = models.ManyToManyField(Strategy, blank=True, null=True)
    substrategies = models.ManyToManyField(SubStrategy, blank=True, null=True)
    goals = models.ManyToManyField(Goal, blank=True, null=True, verbose_name=u'Goals')
    subgoals = models.ManyToManyField(SubGoal, blank=True, null=True, verbose_name=u'Subgoals')

    equity = models.BooleanField('Equity related')
    equity_comment = models.TextField(null=True, blank=True)

    active = models.BooleanField('Shown on map')

    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    # cached query results
    subregions_string = models.CharField('Subregions', max_length=50, default='')
    lead_dept_string = models.CharField('Lead Depts', max_length=100, default='')
    community_type_string = models.CharField('Community Types', max_length=100, default='')
    nr_subgoals = models.IntegerField('Nr Subgoals', default=0)
    nr_goals = models.IntegerField('Nr Goals', default=0)
    nr_municipalities = models.IntegerField('Nr Municipalities', default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['name']  

    def save(self, *args, **kwargs):

        self.subregions_string = self.get_subregions_string()
        self.lead_dept_string = self.get_lead_dept_string()
        self.community_type_string = self.get_community_type_string()
        self.nr_subgoals = self.get_nr_subgoals()
        self.nr_goals = self.get_nr_goals()
        self.nr_municipalities = self.get_nr_municipalities()

        super(Project, self).save(*args, **kwargs)


    def get_subregions_string(self):
        muni_subregions = [m.subregion.all() for m in self.municipalities.all() for s in m.subregion.all()]
        # flatten list
        subregions = [s.abbr for s in muni_subregions for s in s]
        # remove duplicates (list > set > list)
        subregions = sorted(list(set(subregions)))
        subregions_string = ', '.join(subregions)
        return subregions_string

    def get_lead_dept_string(self):
        depts = [d.name for d in self.lead_dept.all()]
        depts_string = ', '.join(depts)
        return depts_string

    def get_community_type_string(self):
        ct = []
        for m in self.municipalities.all():
            if m.community_type != None:
                ct.append(m.community_type.name)
        # # remove duplicates (list > set > list)
        ct = sorted(list(set(ct)))
        ct_string = ', '.join(ct)
        return ct_string
    # TODO: m2m_changed signal to add supergoals from goals and strategies from substrategies     

    def get_nr_subgoals(self):
        subgoals = self.goals.all()
        return len(subgoals)

    def get_nr_goals(self):
        goals = self.goals.all()
        return len(goals)

    def get_nr_municipalities(self):
        municipalities = self.municipalities.all()
        return len(municipalities)


    
    