
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^blogs', include('apps.blogs.urls')),
    url(r'^surveys', include('apps.surveys.urls')),
    url(r'^users', include('apps.users.urls')),
    url(r'^time_display', include('apps.time_display.urls')),
    url(r'^random_word', include('apps.random_word.urls')),
    url(r'^course', include('apps.course.urls'))
]
