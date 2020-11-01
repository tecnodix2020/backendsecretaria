from django.conf.urls import url
from message import views

urlpatterns = [
  url(r'^messages$', views.messages_list),
  url(r'^messages/store$', views.post_message),
  url(r'^messages/delete/(?P<pk>\d+)$', views.delete_message)
]
