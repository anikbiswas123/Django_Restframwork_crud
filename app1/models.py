from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    Tittle=models.CharField(max_length=80)
    email=models.EmailField(max_length=30)
    
    def __str__(self):
        return str(self.name)
