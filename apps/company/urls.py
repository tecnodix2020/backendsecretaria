from django.conf.urls import url
from apps.company import views


urlpatterns = [
    url(r'^company$', views.companies_list)
]
