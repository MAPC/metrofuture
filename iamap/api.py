from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from iamap.models import Project, CommunityType, Municipality
from iamap.tastyhacks import GeoResource

class ProjectShortResource(ModelResource):
    """
    Only project name to save data and avoid recursive problems.
    There might be a better way to do that, e.g. limit data in related resources.
    """

    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projectshort'
        fields = ['name', 'id', ]
        allowed_methods = ['get']


class MunicipalityResource(GeoResource):
    projects = fields.ToManyField(ProjectShortResource, 'project_set', full=True)

    class Meta:
        queryset = Municipality.objects.filter(project__isnull=False).distinct()
        resource_name = 'municipality'
        allowed_methods = ['get',]
        limit = 200
        filtering = {
            'muni_id': ALL,
            'name': ALL,
            'project': ALL_WITH_RELATIONS,
        }

class CommunityTypeResource(ModelResource):
    class Meta:
        queryset = CommunityType.objects.all()
        resource_name = 'community_type'
        allowed_methods = ['get']
        filtering = {
            'abbr': ALL,
            'name': ALL,
        }

class ProjectResource(ModelResource):
    community_types = fields.ToManyField(CommunityTypeResource, 'community_types', full=True)
    municipalities = fields.ToManyField(MunicipalityResource, 'municipalities', full=True)

    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        fields = ['name']
        # excludes = ['client', 'funding', 'collab_dept', 'collab_ext',]
        allowed_methods = ['get']
        filtering = {
            'active': ALL,
            'name': ALL,
            'community_types': ALL_WITH_RELATIONS,
            'municipalities': ALL_WITH_RELATIONS, 
        }

