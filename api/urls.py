from django.conf.urls import url
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SmartDesk API')

urlpatterns =[
  url(r'^docs$', schema_view),
  url(r'^api/visits$', views.visits_list),
  url(r'^api/desk/visits$', views.visits_list_desk),
  url(r'^api/visits/(?P<pk>[0-9]+)$', views.visit_detail)
]