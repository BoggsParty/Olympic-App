from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^(?P<sport_slug>[\w-]+)/$', views.selection, name='selection'),
url(r'^new/$', views.selection, name='new_selection'),
]