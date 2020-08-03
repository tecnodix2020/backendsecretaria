from django.conf.urls import url
from api import views

urlpatterns =[
  url(r'^api/visits$', views.visits_list),
  url(r'^api/visits/(?P<pk>[0-9]+)$', views.visit_detail)
]