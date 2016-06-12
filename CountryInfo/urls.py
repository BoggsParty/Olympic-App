from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^$', views.menu, name='menu'),
url(r'^(?P<sport_slug>[\w-]+)/$', views.detail, name='detail'),
]