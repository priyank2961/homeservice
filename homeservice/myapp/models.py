from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField

# Create your models here.
class CustomerRegModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)

class EmployeeRegModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    working_category=models.CharField(max_length=20)
    experience=models.CharField(max_length=3)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    c_name=models.CharField(max_length=30)
    e_name = models.CharField(max_length=30)
    service=models.CharField(max_length=30)
    problem = models.CharField(max_length=100)
    date=models.CharField(max_length=30)
    time = models.CharField(max_length=30)

class pendingAppointment(models.Model):
    c_name=models.CharField(max_length=30)
    e_name = models.CharField(max_length=30)
    service=models.CharField(max_length=30)
    problem = models.CharField(max_length=100)
    date=models.CharField(max_length=30)
    time = models.CharField(max_length=30)
