from rest_framework import serializers
from app.models import Builder

class BuilderSerializer(serializers.ModelSerializer):
   class Meta:
      model = Builder
      fields = '__all__'