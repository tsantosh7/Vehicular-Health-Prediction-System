from django.conf.urls import patterns, url 

from analysis import views

urlpatterns = patterns('',
		        url(r'^$', views.index, name='index'),
#       url(r'^p1_submit/$', views.p1_submit, name='index'),
			url(r'^analysis$', views.index, name='index'),
			url(r'^analysis/dashboard$', views.dashboard, name='dashboard'),
		)

