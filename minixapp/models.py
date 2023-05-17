from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_address=models.CharField(max_length=100)
    emp_post=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.emp_name)
    
