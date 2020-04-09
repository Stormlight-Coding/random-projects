from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^/register$', views.register),
  url(r'^/login$', views.login),
  url(r'^/logout$', views.logout),
  url(r'^/dashboard$', views.dashboard),
  url(r'^/add$', views.add),
  url(r'^/create$', views.create),
  url(r'^/(?P<book_id>\d+)/book_info$', views.book_info),
  url(r'^/(?P<book_id>\d+)/add_review$', views.add_review),
  ]
