from django.shortcuts import render
from .models import *
from django.http import JsonResponse

from .serializers import studentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def get_student(request):
    obj = Student.objects.all()
    serilizer = studentSerializer(obj, many=True)
    return Response( serilizer.data)



@api_view(['POST'])
def add_student(request):
    
    serializer=studentSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def studentDetalis(request, id):
    task_ob = Student.objects.get(id=id)
    serilizer = studentSerializer(task_ob, many=False)
    return Response(serilizer.data)


@api_view(['POST'])# post ,put,patch
def student_update(request,id):
    task=Student.objects.get(id=id)
    serilizer=studentSerializer(instance=task,data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['DELETE'])
def Delete_std(request,id):
    std=Student.objects.get(id=id)
    std.delete()
    return Response("Deleting Item successfully")

     


    
