from rest_framework import serializers
from .models import *


class PartnerSerializer(serializers.ModelSerializer):
          class Meta:
                model  = Partners
                fields  = ['image', 'name', 'body', 'number', 'url_name', 'email']