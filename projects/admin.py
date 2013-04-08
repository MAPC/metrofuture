from django.contrib.gis import admin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django import forms

import reversion
import csv

from projects.models import Project, Subregion, CommunityType, Strategy, Goal, SubGoal, Municipality, Department, Funding, SubStrategy


CSV_FIELD_NAMES = {
    'projects.project': ['pk', 'name', 'status', 'lead_dept_string', 'subregions_string', 'community_type_string', 'nr_goals', 'nr_subgoals', 'nr_municipalities', 'last_modified', ]
}


def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """

    if not request.user.is_staff:
        raise PermissionDenied

    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    writer = csv.writer(response)

    field_names = CSV_FIELD_NAMES.get(unicode(opts), [field.name for field in opts.fields])
    
    # Write a first row with header information
    writer.writerow(field_names)
    
    # Write data rows
    for obj in queryset:
        try:
            writer.writerow([getattr(obj, field) for field in field_names])
        except UnicodeEncodeError:
            # Log error in export file
            # FIXME: force proper encoding
            row = [ '-' for field in field_names ]
            row[0] = 'Error: Could not export data for %i.' % (obj.id)
            writer.writerow(row)

    return response

export_as_csv.short_description = _('Export selected %(verbose_name_plural)s as CSV file')


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project

    def clean_end_date(self):
        # validates data
        date = self.cleaned_data['end_date']
        status = self.cleaned_data['status']
        if date == None and status == 'com':
            raise forms.ValidationError("Project complete, please provide an end date.")
        return date


class ProjectAdmin(reversion.VersionAdmin):

    form = ProjectAdminForm

    fieldsets = [
        (None, 
            {'fields': ['name', 'desc', 'url', 'thumbnail', 'active', ]}),
        ('MetroFuture', 
            {'fields': ['strategies', 'substrategies', 'goals', 'subgoals',]}),
        ('Collaborations', 
            {'fields': ['lead_dept', 'collab_dept', 'collab_ext', 'client', 'funding', ]}),
        ('Regional properties',
            {'fields': ['municipalities_type', 'municipalities', 'subregions_string', 'community_type_string', ]}),
        ('Other project properties',
            {'fields': ['timing', 'status', 'start_date', 'end_date', 'equity', 'equity_comment', ]}),
    ]    
    list_filter = ['municipalities__subregion', 'municipalities', 'municipalities__community_type', 'municipalities_type', 'lead_dept', 'status', 'goals', 'strategies', ]
    date_hierarchy = 'last_modified'
    list_display = ('pk', 'name', 'desc', 'status', 'lead_dept_string', 'subregions_string', 'community_type_string', 'get_nr_goals', 'get_nr_subgoals', 'get_nr_municipalities', 'last_modified',)   
    list_editable = ('name', 'desc', 'status', )
    search_fields = ['name', 'desc']
    ordering = ['id']
    readonly_fields = ('subregions_string', 'community_type_string',)
    actions = [export_as_csv]

    def lead_dept_string(self, obj):
        return obj.lead_dept_string
    lead_dept_string.short_description = 'Lead Depts'

    def subregions_string(self, obj):
        return obj.subregions_string
    subregions_string.short_description = 'Subregions'

    def community_type_string(self, obj):
        return obj.community_type_string
    community_type_string.short_description = 'Community Types'

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
    exclude = ('geometry',)

class CommunityTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'abbr', 'name', )
    list_editable = ('abbr', 'name', )

class SubGoalAdmin(admin.TabularInline):
    fields = ('nr', 'title', )
    ordering = ['nr']
    model = SubGoal

class GoalAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SubGoalAdmin]

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
admin.site.register(Goal, GoalAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Funding, FundingAdmin)
admin.site.register(Department, DepartmentAdmin)
