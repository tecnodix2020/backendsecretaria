from django.conf.urls import url
from visit import views

urlpatterns = [
  url(r'^api/visits$', views.visits_list),
  url(r'^api/packages$', views.packages_list),
  url(r'^api/desk/visits$', views.visits_list_desk),
  url(r'^api/visits/(?P<pk>[0-9]+)$', views.visit_detail),

  url(r'^visits$', views.get_visits_by_type)
]
