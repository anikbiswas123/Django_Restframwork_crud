from django.db import models



# Create your models here.
class Student(models.Model):
    std_name=models.CharField(max_length=140)
    std_dept=models.CharField(max_length=20)
    std_email=models.EmailField(max_length=30)
    std_address=models.CharField(max_length=150)
    
    def __str__(self) :
        return str(self.std_name)
