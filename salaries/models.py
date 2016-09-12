from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    ethnicity = models.CharField(max_length=100)
    gender = models.CharField(max_length=2)
    age = models.IntegerField()
    years_experience = models.IntegerField()
    role = models.CharField(max_length=100)

class EmployeeData(models.Model):
    employee_info = models.CharField(max_length=1000)
