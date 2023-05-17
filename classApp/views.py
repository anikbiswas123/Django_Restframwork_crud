from .models import Person
from .serializers import PersonSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated






# Create your views here.

class person_list(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,format=None):
        obj=Person.objects.all()
        serializer=PersonSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request,formate=None):
        serializer=PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class personDetalis(APIView):
    
    def get_object(pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None):
        obj=self.get_object(pk=pk)
        serializer=PersonSerializer(obj,many=False)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        obj=self.get_object(pk=pk)
        serializer=PersonSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=True):
        obj=self.get_object(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
       
        
    
            
    
    
