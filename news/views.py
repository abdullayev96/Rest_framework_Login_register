from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from  rest_framework import status
from rest_framework.generics import ListAPIView



class NewsApi(APIView):
      def get(self, request, *args, **kwargs):
          news  = News.objects.all()
          serializers = NewsSerializer(news, many=True, context={'request':self.request})
          return Response({"data":serializers.data})



class NewsBabyApi(APIView):
      def get(self, request, *args, **kwargs):
          baby  = BigNewsBaby.objects.all()
          serializers = BabySerializer(baby, many=True, context={'request':self.request})
          return Response({"data":serializers.data})




def get_client_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class NewsDetail(APIView):

          # def get(self, request, pk=None):
          #     if pk:
          #        user = News.objects.get(id=pk)
          #        serializer = NewsDetailSerializers(user, context={'request': self.request})
          #        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
          #
          #     user = News.objects.all()
          #     serializer = NewsSerializer(user, many=True)
          #     return Response({"data": serializer.data}, status=status.HTTP_200_OK)

          def get(self, request, pk, *args, **kwargs):
              ip = get_client_ip(self.request)

              if IpModel.objects.filter(ip=ip).exists():
                 new_id = pk
                 new = News.objects.get(pk=new_id)
                 new.views.add(IpModel.objects.get(ip=ip))

              else:
                 IpModel.objects.create(ip=ip)
                 new_id = request.GET.get('pk')
                 new = News.objects.get(pk=new_id)
                 new.views.add(IpModel.objects.get(ip=ip))
              serializers = NewsDetailSerializers(new, context={'request':self.request})

              return Response(serializers.data)


