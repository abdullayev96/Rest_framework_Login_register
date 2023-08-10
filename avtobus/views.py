from django.shortcuts import render

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView



class AvtobusApi(ListAPIView):
          queryset = AvtobusYear.objects.all()
          serializer_class = AvtobusYearSerializer
          permission_classes = [IsAuthenticatedOrReadOnly]


class AvtobusDetail(RetrieveAPIView):
          queryset =AvtobusYear.objects.all()
          serializer_class = AvtobusYearDetailSerializer
          permission_classes = [AllowAny]




class AvtobusBackApi(ListAPIView):
          queryset = AvtobusBackground.objects.all()
          serializer_class = AvtoBackSerializer
          permission_classes = [IsAuthenticatedOrReadOnly]



class AvtoDataApi(ListAPIView):
          queryset = AvtobusData.objects.all()
          serializer_class = AvtoDataSerializer
          permission_classes = [IsAuthenticatedOrReadOnly]





class BusOrderApi(ListAPIView):
          queryset = BusOrder.objects.all()
          serializer_class = BusListSerializer
          permission_classes = [AllowAny]





class BusOrderPostApi(CreateAPIView):
          queryset = OrderPost.objects.all()
          serializer_class = OrderPostSerializer
          permission_classes = [AllowAny]


# class BusCardApi(APIView):
#       def get(self, request):
#           card  = BusCard.objects.all()
#           serializers  = CardSerializer(card, many=True)
#           return Response({"card":serializers.data})

class BusCardApi(ListAPIView):
          queryset = BusCard.objects.all()
          serializer_class = CardSerializer
          permission_classes = [AllowAny]

