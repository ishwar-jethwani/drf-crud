from rest_framework.serializers import ModelSerializer
from .models import *

class EmployeeSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Employee

class TaskSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Task
