from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^eventing/$', views.selection_eventing, name='selection_eventing'),
url(r'^womens-all-around-gymnastics/$', views.selection_womens_all_around_gymnastics, name='selection_womens-all-around-gymnastics'),
url(r'^mens-all-around-gymnastics/$', views.selection_mens_all_around_gymnastics, name='selection_mens_all_around_gymnastics'),
url(r'^womens-track-4x100-relay/$', views.selection_womens_track_4x100_relay, name='selection_womens_track_4x100_relay'),
url(r'^mens-track-4x100-relay/$', views.selection_mens_track_4x100_relay, name='selection_mens_track_4x100_relay'),
url(r'^womens-decathalon/$', views.selection_womens_decathalon, name='selection_womens_decathalon'),
url(r'^mens-decathalon/$', views.selection_mens_decathalon, name='selection_mens_decathalon'),
url(r'^womens-swimming-4x100-medley-relay/$', views.selection_womens_swimming_4x100_medley_relay, name='selection_womens_swimming_4x100_medley_relay'),
url(r'^mens-swimming-4x100-medley-relay/$', views.selection_mens_swimming_4x100_medley_relay, name='selection_mens_swimming_4x100_medley_relay'),
url(r'^womens-swimming-200m-backstroke/$', views.selection_womens_swimming_200m_backstroke, name='selection_womens_swimming_200m_backstroke'),
url(r'^mens-swimming-200m-freestyle/$', views.selection_mens_swimming_1500m_freestyle, name='selection_mens_swimming_1500m_freestyle'),
url(r'^mens-golf/$', views.selection_mens_golf, name='selection_mens_golf'),
url(r'^womens-basketball/$', views.selection_womens_basketball, name='selection_womens_basketball'),
url(r'^womens-soccer/$', views.selection_womens_soccer, name='selection_womens_soccer'),
url(r'^mens-soccer/$', views.selection_mens_soccer, name='selection_mens_soccer'),
url(r'^womens-beach-volleyball/$', views.selection_womens_beach_volleyball, name='selection_womens_beach_volleyball'),
url(r'^mens-waterpolo/$', views.selection_mens_waterpolo, name='selection_mens_waterpolo'),
url(r'^womens-bmx/$', views.selection_womens_bmx, name='selection_womens_bmx'),
url(r'^mens-bmx/$', views.selection_mens_bmx, name='selection_mens_bmx'),
url(r'^mens-handball/$', views.selection_mens_handball, name='selection_mens_handball'),
url(r'^show-jumping/$', views.selection_mens_handball, name='selection_show_jumping'),
]