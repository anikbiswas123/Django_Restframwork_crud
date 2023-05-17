

from rest_framework  import serializers
from .models import *


# class ContactSerializers(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     Tittle=serializers.CharField(max_length=80)
#     email=serializers.EmailField(max_length=30)
    
#     def create(self, validated_data):
        
#       return Contact.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
        
#         instance.name = validated_data.get('name', instance.title)
#         instance.Tittle = validated_data.get('Tittle', instance.title)
#         instance.email = validated_data.get('email', instance.title)
#         instance.save()
#         return instance
    
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'