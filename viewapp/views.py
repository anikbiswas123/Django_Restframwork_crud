

from django.shortcuts import get_object_or_404
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class emloyeeViewSet(viewsets.ViewSet):
   
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(user)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=EmployeeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
        
    def update(self, request, pk=None):
        obj=Employee.objects.get(pk=pk)
        
        serializer=EmployeeSerializer(instance=obj,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        obj=Employee.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   
       
        