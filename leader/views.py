from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from hitcount.views  import HitCountJSONView



class LeaderApi(ListAPIView):
          queryset = Leader.objects.all()
          serializer_class = LeaderSerializer
          permission_classes = [IsAuthenticatedOrReadOnly]



class LeaderDetail(RetrieveAPIView):
          queryset = Leader.objects.all()
          serializer_class = LeaderDetailSerializer
          permission_classes = [IsAuthenticatedOrReadOnly]

