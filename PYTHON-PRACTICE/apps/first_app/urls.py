from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^survey$', views.survey),
    url(r'^survey_results$', views.survey_results),
    url(r'^survey_form$', views.survey_form),
    url(r'^random$', views.random),
    url(r'^session_words$', views.session_words),
    url(r'^add_word$', views.add_word),
    url(r'^clear_words$', views.clear_words),
    url(r'^generate$', views.generate),
    url(r'^clear$', views.clear),
    url(r'^amadon_homepage$', views.amadon_homepage),
    url(r'^buy$', views.buy),
    url(r'^amadon_cart$', views.amadon_cart),
    url(r'^logout$', views.logout),
]
