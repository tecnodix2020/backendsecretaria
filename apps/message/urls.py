from django.conf.urls import url
from apps.message import views

urlpatterns = [
  url(r'^messages$', views.messages_list),
  url(r'^messages/delete/(?P<pk>\d+)$', views.delete_message)
]
