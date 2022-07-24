from django.urls import path
from .views import *

urlpatterns = [
    path("",AddEmployee.as_view(),name="add_employee"),
    path("api/",AddTask.as_view(),name="add_task"),
    path("emplyee_detail/<int:id>/",EmployeeDetail.as_view(),name="emplyee_detail"),
    path("task_detail/<int:id>/",TaskDetail.as_view(),name="task_detail")

]