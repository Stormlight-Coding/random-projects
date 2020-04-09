from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/new$', views.new),
	url(r'^$', views.index),
    url(r'^/create$', views.create),
	url(r'^/(?P<user_id>\d+)/show$', views.show),
	url(r'^/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^/(?P<user_id>\d+)/change$', views.change),
	url(r'^/(?P<user_id>\d+)/delete$', views.delete)
  ]
