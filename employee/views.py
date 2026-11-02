from django.shortcuts import render
from employee.models import User,Employee,EmpTask
from employee.serializers import UserSerializer,EmployeeSerializer,EmpTaskSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class SignUpViewSet(ViewSet):
    def create(self,request):
        print(request.data)
        dser=UserSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeCreate(CreateAPIView,ListAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

class EmployeeidRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

class TaskCreate(CreateAPIView,ListAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=EmpTaskSerializer
    queryset=EmpTask.objects.all()

class TaskRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()