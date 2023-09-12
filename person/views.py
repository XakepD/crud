from django.shortcuts import render
from rest_framework import views, response
from .models import *
from .serializers import *

from rest_framework.decorators import api_view

@api_view(['GET'])
def PersonList(request):
    names = Person.objects.all()
    serializer = NameSerializer(names, many=True)
    return response.Response(serializer.data)
@api_view(['GET'])
def PersonDetail(request, pk):
    name = Person.objects.get(pk=pk)
    serializer = NameSerializer(name, many=False)
    return response.Response(serializer.data)
@api_view(['POST'])
def PersonCreate(request):
    name = Person.objects.all()
    serializer = NameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)
@api_view(['POST'])
def PersonUpdate(request, pk):
    name = Person.objects.get(pk=pk)
    serializer = NameSerializer(instance=name, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)
@api_view(['GET','DELETE'])
def PersonDelete(request, pk):
    name = Person.objects.get(pk=pk)
    name.delete()
    return response.Response("Name Deleted Successfully")