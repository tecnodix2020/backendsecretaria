from django.conf.urls import url
from apps.message import views

urlpatterns = [
  url(r'^message(:?/(?P<pk>\d+))?/$', views.messages_list)
]
