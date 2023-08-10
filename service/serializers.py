from rest_framework import serializers
from .models import *



class ServiceSerializer(serializers.ModelSerializer):
      class Meta:
            model   = ServiceName
            fields  = ['id', 'name']


class ServiceDetailSerializer(serializers.ModelSerializer):
      class Meta:
            model  = ServiceName
            fields  = ['name', 'image','full_name', 'position', 'email', 'number', 'title']