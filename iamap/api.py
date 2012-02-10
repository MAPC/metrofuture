from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from iamap.models import Project, Strategy, Municipality, Goal, Supergoal
from iamap.tastyhacks import GeoResource


class MunicipalityResource(GeoResource):
    projects = fields.ToManyField('iamap.api.ProjectShortResource', 'projects', full=True)

    class Meta:
        queryset = Municipality.objects.filter(projects__isnull=False).distinct()
        resource_name = 'municipality'
        allowed_methods = ['get',]
        limit = 200
        filtering = {
            'muni_id': ALL,
            'name': ALL,
            'projects': ALL_WITH_RELATIONS,
        }

class StrategyResource(ModelResource):
    class Meta:
        queryset = Strategy.objects.all()
        resource_name = 'strategy'
        allowed_methods = ['get']
        filtering = {
            'nr': ALL,
            'name': ALL,
        }

class GoalResource(ModelResource):
    class Meta:
        queryset = Goal.objects.all()
        resource_name = 'goal'
        allowed_methods = ['get']
        filtering = {
            'nr': ALL,
            'title': ALL,
        }

class SupergoalResource(ModelResource):
    class Meta:
        queryset = Supergoal.objects.all()
        resource_name = 'supergoal'
        allowed_methods = ['get']
        filtering = {
            'abbr': ALL,
            'title': ALL,
        }

class ProjectResource(ModelResource):
    municipalities = fields.ToManyField(MunicipalityResource, 'municipalities', full=True)
    strategies = fields.ToManyField(StrategyResource, 'strategies', full=True)
    goals = fields.ToManyField(GoalResource, 'goals', full=True)
    supergoals = fields.ToManyField(SupergoalResource, 'supergoals', full=True)

    class Meta:
        queryset = Project.objects.all().distinct()
        resource_name = 'project'
        fields = ['id','name',]
        limit = 200
        allowed_methods = ['get']
        filtering = {
            'active': ALL,
            'name': ALL,
            'municipalities': ALL_WITH_RELATIONS, 
            'strategies': ALL_WITH_RELATIONS,
            'goals': ALL_WITH_RELATIONS,
            'supergoals': ALL_WITH_RELATIONS,
        }

class ProjectShortResource(ModelResource):
    """
    Short project resource without municipalities to save some size in the 
    GeoJSON results.
    """

    strategies = fields.ToManyField(StrategyResource, 'strategies', full=True)
    goals = fields.ToManyField(GoalResource, 'goals', full=True)
    supergoals = fields.ToManyField(SupergoalResource, 'supergoals', full=True)

    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projectshort'
        fields = ['name', 'id', ]
        limit = 200
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'name': ALL,
            'strategies': ALL_WITH_RELATIONS,
            'goals': ALL_WITH_RELATIONS,
            'supergoals': ALL_WITH_RELATIONS,
        }
