from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from iamap.models import Project, Strategy, SubStrategy, Municipality, Goal, Supergoal, Subregion
from iamap.tastyhacks import GeoResource


class SubregionResource(ModelResource):

    municipalities = fields.CharField(attribute='muni_string')

    class Meta:
        queryset = Subregion.objects.all()
        resource_name = 'subregions'
        allowed_methods = ['get', ]
        include_resource_uri = False
        filtering = {
            'abbr': ALL,
            'name': ALL,
        }
        

class MunicipalityGeoResource(GeoResource):
    """
    GeoJSON enabled municipality result.
    FIXME: projects should be filtered by active=True
    """

    projects = fields.ToManyField('iamap.api.ProjectResource', 'projects', full=True)
    subregion = fields.ToManyField('iamap.api.SubregionResource', 'subregion', full=True)

    class Meta:
        queryset = Municipality.objects.filter(projects__active=True).distinct()
        resource_name = 'municipalities'
        allowed_methods = ['get',]
        limit = 200
        filtering = {
            'muni_id': ALL,
            'name': ALL,
            'projects': ALL_WITH_RELATIONS,
            'subregion': ALL_WITH_RELATIONS,
        }


class MunicipalityResource(ModelResource):
    """
    Municipality short-info without geometry as property in Project Muni List.
    """

    subregion = fields.ToManyField('iamap.api.SubregionResource', 'subregion', full=True)

    class Meta:
        queryset = Municipality.objects.filter(projects__active=True).distinct()
        allowed_methods = ['get',]
        excludes = ['geometry',]
        limit = 200
        filtering = {
            'muni_id': ALL,
            'name': ALL,
            'subregion': ALL_WITH_RELATIONS,
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

class SubStrategyResource(ModelResource):
    class Meta:
        queryset = SubStrategy.objects.all()
        resource_name = 'substrategy'
        allowed_methods = ['get']
        filtering = {
            'letter': ALL,
            'title': ALL,
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

class ProjectMuniResource(ModelResource):
    """
    All Project details without geometry.
    """

    municipalities = fields.ToManyField(MunicipalityResource, 'municipalities', full=True)
    strategies = fields.ToManyField(StrategyResource, 'strategies', full=True)
    substrategies = fields.ToManyField(SubStrategyResource, 'substrategies', full=True)
    goals = fields.ToManyField(GoalResource, 'goals', full=True)
    supergoals = fields.ToManyField(SupergoalResource, 'supergoals', full=True)

    class Meta:
        queryset = Project.objects.filter(active=True).distinct()
        resource_name = 'projects'
        fields = ['id', 'name', 'url', 'desc', 'thumbnail', 'status', ]
        limit = 200
        allowed_methods = ['get']
        filtering = {
            'active': ALL,
            'name': ALL,
            'municipalities': ALL_WITH_RELATIONS, 
            'strategies': ALL_WITH_RELATIONS,
            'substrategies': ALL_WITH_RELATIONS,
            'goals': ALL_WITH_RELATIONS,
            'supergoals': ALL_WITH_RELATIONS,
            'status': ALL,
        }

class ProjectResource(ModelResource):
    """
    Project short-info as property in municipality.
    """

    strategies = fields.ToManyField(StrategyResource, 'strategies', full=True)
    substrategies = fields.ToManyField(SubStrategyResource, 'substrategies', full=True)
    goals = fields.ToManyField(GoalResource, 'goals', full=True)
    supergoals = fields.ToManyField(SupergoalResource, 'supergoals', full=True)

    class Meta:
        queryset = Project.objects.filter(active=True)
        fields = ['name', 'id', 'status', 'active', ]
        limit = 200
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'name': ALL,
            'strategies': ALL_WITH_RELATIONS,
            'substrategies': ALL_WITH_RELATIONS,
            'goals': ALL_WITH_RELATIONS,
            'supergoals': ALL_WITH_RELATIONS,
            'status': ALL,
            'lead_dept': ALL,
            'collab_dept': ALL,
        }
