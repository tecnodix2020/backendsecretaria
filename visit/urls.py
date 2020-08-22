from django.conf.urls import url
from visit import views

urlpatterns = [
  url(r'^api/visits$', views.visits_list),
  url(r'^api/packages$', views.packages_list),
  url(r'^api/desk/visits$', views.visits_list_desk),
  url(r'^api/visits/(?P<pk>[0-9]+)$', views.visit_detail),

  url(r'^visits$', views.get_visits_by_type),
  url(r'^visits/top3$', views.get_top3_of_visits),
  url(r'^packages/employees', views.get_employees_waiting_packages),
  url(r'^visits/employee$', views.get_employee_visit),
  url(r'^visits/employees', views.get_employees_visits)
]
