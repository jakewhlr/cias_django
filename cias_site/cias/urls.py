from django.conf.urls import re_path, url
from cias import views
from fcm_django.api.rest_framework import FCMDeviceViewSet

urlpatterns = [
    re_path('^$', views.default),
    re_path('^info/$', views.info),
    re_path('^info/team/$', views.team),
    re_path('^info/course/$', views.course),
    re_path('^info/documents/$', views.documents),
    re_path('^info/pictures/$', views.pictures),
    re_path('^events/$', views.event_list),
    re_path('^events/recent/$', views.recent_event_list),
    re_path('^events/(?P<pk>[0000-9999]+)/$', views.event_detail),
    re_path('^players/$', views.player_list),
    re_path('^players/(?P<pk>[0000-9999]+)/$', views.player_detail),
    re_path('^players/(?P<pk>[0000-9999]+)/events/$', views.player_event_list),
    re_path('^players/(?P<pk>[0000-9999]+)/events/recent/$', views.player_recent_event_list),
    re_path('^players/(?P<pk>[0000-9999]+)/events/recent/json/$', views.player_recent_event_json),
    re_path('^players/(?P<pk>[0000-9999]+)/events/recent/graph/$', views.player_recent_event_graph),
    re_path('^events/recent/graph/$', views.recent_event_graph),
    url(r'^devices?$', FCMDeviceViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
#    re_path('^coaches/(?P<pk>[0000-9999]+)/$', views.coach_post),
]
