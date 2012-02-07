from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from map.models import Project, CommunityType

class CommunityTypeResource(ModelResource):
    class Meta:
        queryset = CommunityType.objects.all()
        resource_name = 'community_types'
        allowed_methods = ['get']
        filtering = {
            'abbr': ALL,
            'name': ALL,
        }

class ProjectResource(ModelResource):
    community_types = fields.ManyToManyField(CommunityTypeResource, 'community_types')

    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        excludes = ['client', 'funding', 'collab_dept', 'collab_ext',]
        allowed_methods = ['get']
        filtering = {
            'active': ALL,
            'name': ALL,
            'community_types': ALL_WITH_RELATIONS,
        }