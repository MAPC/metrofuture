from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# from django.conf import settings
# from tastypie.api import Api
# from metrofuture.api import SubregionResource, MunicipalityGeoResource, MunicipalityResource, StrategyResource, SubStrategyResource, GoalResource, SupergoalResource, ProjectMuniResource, ProjectResource

# v1_api = Api(api_name='v1')
# v1_api.register(ProjectResource())
# v1_api.register(SubregionResource())
# v1_api.register(MunicipalityGeoResource())
# v1_api.register(MunicipalityResource())
# v1_api.register(StrategyResource())
# v1_api.register(SubStrategyResource())
# v1_api.register(GoalResource())
# v1_api.register(SupergoalResource())
# v1_api.register(ProjectMuniResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'metrofuture.views.home', name='home'),
    # url(r'^metrofuture/', include('metrofuture.foo.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # returns all project filters
    url(r'^filters/$', 'projects.views.get_filters'),

    # returns all projects
    url(r'^projects/$', 'projects.views.all', name='all'),

    # API urls
  #  (r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^grappelli/', include('grappelli.urls')),
)
