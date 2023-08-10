from django.shortcuts import render
from .models import ServiceName
from .serializers import *
from rest_framework.views import APIView, Response


class ListServiceApi(APIView):
      def get(self, request):
          services  = ServiceName.objects.all()
          serializers  = ServiceSerializer(services, many=True)
          return Response({"services":serializers.data})



class DetailServiceApi(APIView):
      def get(self, request, pk=None):
          if pk:
             user = ServiceName.objects.get(id=pk)
             serializer = ServiceDetailSerializer(user)
             return Response({"status": serializer.data})

          user = ServiceName.objects.all()
          serializer = ServiceDetailSerializer(user, many=True)
          return Response({"data": serializer.data}, status=status.HTTP_200_OK)




