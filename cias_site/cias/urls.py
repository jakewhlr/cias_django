from django.conf.urls import re_path, url
from cias import views
from fcm_django.api.rest_framework import FCMDeviceViewSet

urlpatterns = [
    re_path('^events/$', views.event_list),
    re_path('^events/recent/$', views.recent_event_list),
    re_path('^events/(?P<pk>[0000-9999]+)/$', views.event_detail),
    re_path('^players/$', views.player_list),
    re_path('^players/(?P<pk>[0000-9999]+)/$', views.player_detail),
    re_path('^players/(?P<pk>[0000-9999]+)/events/$', views.player_event_list),
    url(r'^devices?$', FCMDeviceViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]
