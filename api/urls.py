from django.conf.urls import url
from api import views

urlpatterns =[
  url(r'^api/visits$', views.visits_list),
  url(r'^api/packages$', views.packages_list),
  url(r'^api/desk/visits$', views.visits_list_desk),
  url(r'^api/visits/(?P<pk>[0-9]+)$', views.visit_detail)
]