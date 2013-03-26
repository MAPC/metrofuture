from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# from django.conf import settings

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

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^grappelli/', include('grappelli.urls')),
)