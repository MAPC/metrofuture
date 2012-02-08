from iamap.models import Project, Subregion, CommunityType, Strategy, Goal, Supergoal, Municipality
from django.contrib.gis import admin
# from django.contrib.gis import admin


class ProjectAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, 
    #         {'fields': ['name', 'slug', 'survey_active', 'districtid', 'survey_incentive']}),
    #     ('School Database Attributes', 
    #         {'fields': ['schid', 'address', 'town', 'state', 'zip', 'principal', 'phone', 'fax', 'grades', 'schl_type']}),
    #     ('Map',
    #         {'fields': ['geometry', ]}),
    # ]    
    list_filter = ['active']
    list_display = ('pk', 'name', )
    search_fields = ['name']
    ordering = ['id']


class MunicipalityAdmin(admin.OSMGeoAdmin):    
    list_display = ('name', )
    search_fields = ['name', ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Subregion, admin.ModelAdmin)
admin.site.register(CommunityType, admin.ModelAdmin)
admin.site.register(Strategy, admin.ModelAdmin)
admin.site.register(Goal, admin.ModelAdmin)
admin.site.register(Supergoal, admin.ModelAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
