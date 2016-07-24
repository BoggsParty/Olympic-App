from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^all/$', views.all_comments, name='all_comments'),
]