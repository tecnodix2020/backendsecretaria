from django.conf.urls import url
from employeemsg import views

urlpatterns = [
  url(r'^msgsbyemployee$', views.msg_by_employee),
  url(r'^msgsbyemployee/(?P<pk>\w+-\w+-\w+-\w+-\w+)$', views.msg_emp_detail)
]
