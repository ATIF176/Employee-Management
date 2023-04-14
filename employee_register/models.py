from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=11)
    positions = models.ForeignKey(Position, on_delete=models.CASCADE)