from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100) #to store name
    location = models.CharField(max_length=100)
    total_headcount = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100) #to store  name 
    dob = models.DateField() #to store dates
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
