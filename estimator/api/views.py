from django.shortcuts import render
from django.http import JsonResponse
from app.models import Builder
from api.serializers import BuilderSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def builder_list(request):
    if request.method == 'GET':
        builders = Builder.objects.all()
        serializer = BuilderSerializer(builders,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def view_builder(request):
    if request.method == 'GET':
        builders = Builder.objects.all()
        serializer = BuilderSerializer(builders,many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def add_builder(request):
    serializer = BuilderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)