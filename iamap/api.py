from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from iamap.models import Project, CommunityType, Municipality
from iamap.tastyhacks import GeoResource

class MunicipalityResource(GeoResource):
    class Meta:
        queryset = Municipality.objects.all()
        resource_name = 'municipality'
        allowed_methods = ['get',]
        filtering = {
            'muni_id': ALL,
            'name': ALL,
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
        excludes = ['client', 'funding', 'collab_dept', 'collab_ext',]
        allowed_methods = ['get']
        filtering = {
            'active': ALL,
            'name': ALL,
            'community_types': ALL_WITH_RELATIONS,
            'municipalities': ALL_WITH_RELATIONS, 
        }