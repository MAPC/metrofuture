from iamap.models import Project, Subregion, CommunityType, Strategy, Goal, Supergoal, Municipality
from django.contrib.gis import admin
# from django.contrib.gis import admin


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, 
            {'fields': ['name', 'desc', 'url', 'thumbnail', ]}),
        ('MetroFuture', 
            {'fields': ['strategies', 'goals', 'supergoals', ]}),
        ('Collaborations', 
            {'fields': ['lead_dept', 'collab_dept', 'collab_ext', 'client', 'funding', ]}),
        ('Regional properties',
            {'fields': ['municipalities_type', 'municipal_specific', 'community_types', 'municipalities', 'subregions', 'active', ]}),
        ('Other project properties',
            {'fields': ['timing', 'status', 'equity', ]}),
    ]    
    list_filter = ['goals', 'supergoals', 'strategies', ]
    list_display = ('pk', 'name', )
    search_fields = ['name', 'desc']
    ordering = ['id']


class MunicipalityAdmin(admin.OSMGeoAdmin):    
    list_display = ('name', )
    search_fields = ['name', ]


class CommunityTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'name', )
    list_editable = ('abbr', 'name', )


class GoalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nr', 'title', )
    list_editable = ('nr', 'title', )
    ordering = ['id']


class SupergoalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'title', )
    list_editable = ('abbr', 'title', )


class StrategyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nr', 'title', )
    list_editable = ('nr', 'title', )
    ordering = ['id']


class SubregionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'name', )
    list_editable = ('abbr', 'name', )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Subregion, SubregionAdmin)
admin.site.register(CommunityType, CommunityTypeAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Supergoal, SupergoalAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
