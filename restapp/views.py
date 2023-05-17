from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import EmployeeSerializer

# Create your views here.

@api_view(['GET'])
def employee_list(request):
    if request.method=='GET':
         emp=Employee.objects.all()
    serializer=EmployeeSerializer(emp,many=True)
    return Response(serializer.data)

@api_view(['POST'])   
def add_employee(request):
    if request.method=='POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def employee_detalis(request,id):
    emp=Employee.objects.get(id=id)
    serializer=EmployeeSerializer(emp,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def employee_update(request,id):
    emp=Employee.objects.get(id=id)
    serilizer=EmployeeSerializer(instance=emp,data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)


@api_view(['DELETE'])
def employee_delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return Response("Item deleting successfully")
    
    
        
        