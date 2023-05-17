from django.db import models

# Create your models here.
class Person(models.Model):
    p_name=models.CharField(max_length=100)
    p_address=models.CharField(max_length=60)
    p_email=models.EmailField(max_length=35)
    
    
    def __str__(self):
        return str(self.p_name)
