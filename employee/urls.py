from django.conf.urls import url
from employee import views


urlpatterns = [
    url(r'^employees$', views.employees_list)
]
