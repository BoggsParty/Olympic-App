from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^$', views.menu, name='menu'),
url(r'^eventing/$', views.eventing_detail, name='eventing_detail'),
url(r'^womens-all-around-gymnastics/$', views.womens_all_around_gymnastics_detail, name='womens-all-around-gymnastics_detail'),
url(r'^mens-all-around-gymnastics/$', views.mens_all_around_gymnastics_detail, name='mens_all_around_gymnastics_detail'),
url(r'^womens-track-4x100-relay/$', views.womens_track_4x100_relay_detail, name='womens_track_4x100_relay_detail'),
url(r'^mens-track-4x100-relay/$', views.mens_track_4x100_relay_detail, name='mens_track_4x100_relay_detail'),
url(r'^womens-3000m-steeplechase/$', views.womens_decathalon_detail, name='womens_decathalon_detail'),
url(r'^mens-3000m-steeplechase/$', views.mens_decathalon_detail, name='mens_decathalon_detail'),
url(r'^womens-swimming-4x100-medley-relay/$', views.womens_swimming_4x100_medley_relay_detail, name='womens_swimming_4x100_medley_relay_detail'),
url(r'^mens-swimming-4x100-medley-relay/$', views.mens_swimming_4x100_medley_relay_detail, name='mens_swimming_4x100_medley_relay_detail'),
url(r'^womens-swimming-200m-backstroke/$', views.womens_swimming_200m_backstroke_detail, name='womens_swimming_200m_backstroke_detail'),
url(r'^mens-swimming-200m-IM/$', views.mens_swimming_1500m_freestyle_detail, name='mens_swimming_1500m_freestyle_detail'),
url(r'^mens-golf/$', views.mens_golf_detail, name='mens_golf_detail'),
url(r'^womens-basketball/$', views.womens_basketball_detail, name='womens_basketball_detail'),
url(r'^womens-soccer/$', views.womens_soccer_detail, name='womens_soccer_detail'),
url(r'^mens-soccer/$', views.mens_soccer_detail, name='mens_soccer_detail'),
url(r'^womens-beach-volleyball/$', views.womens_beach_volleyball_detail, name='womens_beach_volleyball_detail'),
url(r'^mens-waterpolo/$', views.mens_waterpolo_detail, name='mens_waterpolo_detail'),
url(r'^womens-bmx/$', views.womens_bmx_detail, name='womens_bmx_detail'),
url(r'^mens-bmx/$', views.mens_bmx_detail, name='mens_bmx_detail'),
url(r'^mens-handball/$', views.mens_handball_detail, name='mens_handball_detail'),
url(r'^show-jumping/$', views.show_jumping_detail, name='show_jumping_detail'),
]