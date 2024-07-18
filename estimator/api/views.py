from django.shortcuts import render
from django.http import JsonResponse
from app.models import Builder
from api.serializers import BuilderSerializer

# Create your views here.
def builder_list(request):
    if request.method == 'GET':
        builders = Builder.objects.all()
        serializer = BuilderSerializer(builders,many=True)
        return JsonResponse(serializer.data, safe=False)