from django.conf.urls import url
from user import views


urlpatterns = [
    url(r'^users$', views.users_list),
    url(r'^login$', views.authenticate)
]
