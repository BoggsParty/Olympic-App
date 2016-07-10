from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^$', views.dashboard, name='dashboard'),
url(r'^view-all/$', views.view_all, name='view_all'),
url(r'^view-all/eventing', views.view_all_1, name='view_all_1'),
#url(r'^view-all/show-jumping', views.view_all_2, name='view_all_2'),
#url(r'^view-all/womens-beach-volleyball', views.view_all_3, name='view_all_3'),
#url(r'^view-all/mens-waterpolo', views.view_all_4, name='view_all_4'),
#url(r'^view-all/womens-bmx', views.view_all_5, name='view_all_5'),
#url(r'^view-all/mens-bmx', views.view_all_6, name='view_all_6'),
#url(r'^view-all/womens-basketball', views.view_all_7, name='view_all_7'),
#url(r'^view-all/mens-handball', views.view_all_8, name='view_all_8'),
#url(r'^view-all/womens-swimming-4x100-medley-relay', views.view_all_9, name='view_all_9'),
#url(r'^view-all/womens-swimming-200m-backstroke', views.view_all_11, name='view_all_11'),
#url(r'^view-all/mens-swimming-200m-freestyle', views.view_all_12, name='view_all_12'),
#url(r'^view-all/womens-3000m-steeplechase', views.view_all_13, name='view_all_13'),
#url(r'^view-all/mens-3000m-steeplechase', views.view_all_14, name='view_all_14'),
#url(r'^view-all/womens-track-4x100-relay', views.view_all_15, name='view_all_15'),
#url(r'^view-all/mens-track-4x100-relay', views.view_all_16, name='view_all_16'),
#url(r'^view-all/womens-soccer', views.view_all_17, name='view_all_17'),
#url(r'^view-all/mens-soccer', views.view_all_18, name='view_all_18'),
#url(r'^view-all/womens-all-around-gymnastics', views.view_all_19, name='view_all_19'),
#url(r'^view-all/mens-all-around-gymnastics', views.view_all_20, name='view_all_20'),
url(r'^register/', views.adduser, name='adduser'),
url(r'^logout/', views.logout_view, name='logout'),
url(r'^reset-password/', views.reset_password, name='password'),
url(r'^password-confirmation/', views.password_confirmation, name='password_confirmation'),
url(r'^retrieve-username/', views.retrieve_username, name='retrieve_username'),
url(r'^retrieve-username-confirmation/', views.retrieve_username_confirmation, name='username_confirmation'),
url(r'^about/', views.about, name='about'),
url(r'^', include('django.contrib.auth.urls')),
url(r'^successful/', views.create_account_success, name='create_account_success'),
url('^create-account/', CreateView.as_view(
        template_name='registration/createaccount.html',
        form_class=UserCreationForm,
        success_url='/successful/'
    )),
]