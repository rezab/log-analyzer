from django.conf.urls import patterns, include, url
from servicelog import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^instance/$', views.servicelists),
    url(r'^instance/(?P<log_name>[-\w]+)/$', views.servicedetails),
)