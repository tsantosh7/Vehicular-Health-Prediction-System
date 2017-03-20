from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *

from analysis import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'analysis_lokalhouse.views.home', name='home'),
	url(r'^$', views.index, name='index'),
	url(r'^analysis/', include('analysis.urls', namespace="analysis")),
    # url(r'^analysis_lokalhouse/', include('analysis_lokalhouse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
