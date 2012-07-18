from iamap.models import Project, Subregion, CommunityType, Strategy, Goal, Supergoal, Municipality, Department, Funding, SubStrategy
from django.contrib.gis import admin

import reversion

class ProjectAdmin(reversion.VersionAdmin):
    fieldsets = [
        (None, 
            {'fields': ['name', 'desc', 'url', 'thumbnail', 'active', ]}),
        ('MetroFuture', 
            {'fields': ['strategies', 'substrategies', 'supergoals', 'goals',]}),
        ('Collaborations', 
            {'fields': ['lead_dept', 'collab_dept', 'collab_ext', 'client', 'funding', ]}),
        ('Regional properties',
            {'fields': ['municipalities_type', 'municipal_specific', 'municipalities', ]}),
        ('Other project properties',
            {'fields': ['timing', 'status', 'equity', ]}),
    ]    
    list_filter = ['supergoals', 'goals', 'strategies', 'lead_dept']
    list_display = ('pk', 'name', 'active', 'status', )
    list_editable = ('name', 'active', 'status', )
    search_fields = ['name', 'desc']
    ordering = ['id']


    def changelist_view(self, request, extra_context=None):

        # requires the "MetroFuture Admin" group
        if not request.GET.has_key('lead_dept__id__in') and not 'MetroFuture Admin' in  request.user.groups.values_list('name', flat=True):

            q = request.GET.copy()
            q['lead_dept__id__in'] = ','.join([str(dept.id) for dept in request.user.get_profile().department.all()])
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()
        return super(ProjectAdmin,self).changelist_view(request, extra_context=extra_context)


class MunicipalityAdmin(admin.OSMGeoAdmin):    
    list_display = ('name', )
    search_fields = ['name', ]

class CommunityTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'name', )
    list_editable = ('abbr', 'name', )

class GoalAdmin(admin.TabularInline):
    fields = ('nr', 'title', )
    ordering = ['nr']
    model = Goal

class SupergoalAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [GoalAdmin]

class SubStrategyAdmin(admin.TabularInline):
    fields = ('letter', 'title', )
    ordering = ['strategy', 'letter', ]
    model = SubStrategy

class StrategyAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines=[SubStrategyAdmin]

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
admin.site.register(Supergoal, SupergoalAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Funding, FundingAdmin)
admin.site.register(Department, DepartmentAdmin)
