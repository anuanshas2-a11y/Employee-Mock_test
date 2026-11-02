from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    department=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    joining_date=models.DateField(auto_now_add=True)

class EmpTask(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    assigned_to=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)

    PRIORITY_CHOICE=[
        ('1','Low'),
        ('2','Medium'),
        ('3','High'),
    ]

    priority=models.CharField(max_length=100,choices=PRIORITY_CHOICE)

    STATUS_CHOICE=[
        ('pending','Pending'),
        ('in progress','In Progress'),
        ('completed','Completed'),
    ]

    status=models.CharField(max_length=100,choices=STATUS_CHOICE,default='in progress')

    due_date=models.DateField(auto_now_add=True)