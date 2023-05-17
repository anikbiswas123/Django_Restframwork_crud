from django.db import models

# Create your models here.
class Person(models.Model):
    p_name=models.CharField(max_length=100)
    p_address=models.CharField(max_length=80)
    p_post=models.CharField(max_length=70)
    
    def __str__(self):
        return self.p_name
    
