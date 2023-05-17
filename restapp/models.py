from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_address=models.CharField(max_length=50)
    emp_post=models.CharField(max_length=20)
    
    def __str__(self):
        return self.emp_name
    
    
