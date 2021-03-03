from django.conf.urls import url
from apps.employee import views


urlpatterns = [
    url(r'^employees$', views.employees_list)
]
