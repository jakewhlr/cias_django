from django.conf.urls import url
from cias import views

urlpatterns = [
    url('events/$', views.event_list),
    url('events/(?P<pk>[0-9][0-9]+)/$', views.event_detail),
]
