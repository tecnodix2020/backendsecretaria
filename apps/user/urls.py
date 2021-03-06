from django.conf.urls import url
from apps.user import views


urlpatterns = [
    url(r'^users$', views.users_list),
    url(r'^users/(?P<pk>\w+-\w+-\w+-\w+-\w+)$', views.user_detail),
    url(r'^auth$', views.authentication)
]
