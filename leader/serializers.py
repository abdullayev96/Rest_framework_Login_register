from rest_framework import serializers
from .models import *



class LeaderSerializer(serializers.ModelSerializer):
          class Meta:
                    model  = Leader
                    fields  = ['id', 'image', 'position', 'tel_num', 'email', 'faks', 'reception_time']


class LeaderDetailSerializer(serializers.ModelSerializer):
          class Meta:
                    model  = Leader
                    fields  = ['name', 'image', 'position', 'email', 'tel_num', 'title']