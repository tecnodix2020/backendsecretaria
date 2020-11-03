from django.conf.urls import url
from visitor import views


urlpatterns = [
    url(r'^visitors$', views.visitors_list),
    url(r'^visitors/(?P<pk>\w+-\w+-\w+-\w+-\w+)$', views.visitor_detail)
]
