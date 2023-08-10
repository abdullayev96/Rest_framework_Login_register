from django.shortcuts import render
from .models import Information
from rest_framework.views import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status


class InformationApi(ListAPIView):
      queryset = Information.objects.all()
      serializer_class = InformationSerializer

      # def get(self, request, *args, **kwargs):
      #     info = Information.objects.all()
      #     serializers = InformationSerializer(info, many=True)
      #     return Response(serializers.data)


