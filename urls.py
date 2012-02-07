from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# API
from tastypie.api import Api
from map.api import ProjectResource, CommunityTypeResource

v1_api = Api(api_name='v1')
v1_api.register(ProjectResource())
v1_api.register(CommunityTypeResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template': 'base.html'}),
    # url(r'^metrofuture/', include('metrofuture.foo.urls')),

    # returns all projects
    url(r'^projects/$', 'map.views.get_projects'),

    # returns all project filters
    url(r'^projects/filters/$', 'map.views.get_filters'),

    # API
    (r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
