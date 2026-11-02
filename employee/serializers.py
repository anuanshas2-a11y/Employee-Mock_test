from rest_framework import serializers
from employee.models import User,Employee,EmpTask
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        
    

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        read_only_fields=["id"]

class EmpTaskSerializer(serializers.ModelSerializer):
    profile=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=EmpTask
        fields="__all__"
        read_only_fields=["id","assigned_to"]

    

