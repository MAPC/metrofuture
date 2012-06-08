from iamap.models import Project, Subregion, CommunityType, Strategy, Goal, Supergoal, Municipality, Department, Funding
from django.contrib.gis import admin
# from django.contrib.gis import admin

import reversion

class ProjectAdmin(reversion.VersionAdmin):
    fieldsets = [
        (None, 
            {'fields': ['name', 'desc', 'url', 'thumbnail', 'active', ]}),
        ('MetroFuture', 
            {'fields': ['strategies', 'goals', 'supergoals', ]}),
        ('Collaborations', 
            {'fields': ['lead_dept', 'collab_dept', 'collab_ext', 'client', 'funding', ]}),
        ('Regional properties',
            {'fields': ['municipalities_type', 'municipal_specific', 'community_types', 'municipalities', 'subregions', ]}),
        ('Other project properties',
            {'fields': ['timing', 'status', 'equity', ]}),
    ]    
    list_filter = ['supergoals', 'goals', 'strategies', ]
    list_display = ('pk', 'name', 'active', 'status', )
    list_editable = ('name', 'active', 'status', )
    search_fields = ['name', 'desc']
    ordering = ['id']


class MunicipalityAdmin(admin.OSMGeoAdmin):    
    list_display = ('name', )
    search_fields = ['name', ]


class CommunityTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'name', )
    list_editable = ('abbr', 'name', )


class GoalAdmin(admin.ModelAdmin):
    list_display = ('nr', 'title', 'supergoal')
    list_editable = ('title', 'supergoal')
    ordering = ['nr']


class SupergoalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'title', )
    list_editable = ('abbr', 'title', )


class StrategyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nr', 'title', )
    list_editable = ('nr', 'title', )
    ordering = ['nr_int', 'nr_char']


class SubregionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'name', )
    list_editable = ('abbr', 'name', )

class FundingAdmin(reversion.VersionAdmin):
    list_display = ('pk', 'name', )
    list_editable = ('name', )

class DepartmentAdmin(reversion.VersionAdmin):
    list_display = ('pk', 'name', )
    list_editable = ('name', )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Subregion, SubregionAdmin)
admin.site.register(CommunityType, CommunityTypeAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Supergoal, SupergoalAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Funding, FundingAdmin)
admin.site.register(Department, DepartmentAdmin)
