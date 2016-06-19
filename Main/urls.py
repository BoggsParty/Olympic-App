from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^$', views.dashboard, name='dashboard'),
url(r'^view-all/', views.view_all, name='view_all'),
url(r'^register/', views.adduser, name='adduser'),
#url(r'^register2/', views.create_choice_record, name='createchoice'),
url(r'^logout/', views.logout_view, name='logout'),
url(r'^reset-password/', views.reset_password, name='password'),
url(r'^password-confirmation/', views.password_confirmation, name='password_confirmation'),
url(r'^retrieve-username/', views.retrieve_username, name='retrieve_username'),
url(r'^retrieve-username-confirmation/', views.retrieve_username_confirmation, name='username_confirmation'),
url(r'^', include('django.contrib.auth.urls')),
url('^create-account/', CreateView.as_view(
        template_name='registration/createaccount.html',
        form_class=UserCreationForm,
        success_url='/register/'
    )),
]