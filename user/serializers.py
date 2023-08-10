from rest_framework import serializers
from .models import *


class SendUserSerializer(serializers.ModelSerializer):
          class Meta:
              model  = SendUser
              fields = ['full_name', 'number', 'email', 'address', 'body',  'file']






class SendBackSerializer(serializers.ModelSerializer):
          class Meta:
              model= SendUser
              fields  = ['reference_number', 'verification_code']



class SendAnswerSerializer(serializers.ModelSerializer):
          class Meta:
              model  = SendUser
              fields = ['reference_number', 'full_name', 'number','address', 'body','created', 'email',  'file', 'status']