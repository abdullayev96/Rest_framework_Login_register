from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView, Response
from rest_framework import status




class VacancyListApi(APIView):
      def get(self, request):
          vacancy  = Vacancy.objects.all()
          serializers   = VacancySerializer(vacancy, many=True)
          return Response({"vacancy":serializers.data})


def get_client_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



class VacancyDetail(APIView):
      def get(self, request, pk, *args, **kwargs):
          ip = get_client_ip(self.request)

          if IpModel.objects.filter(ip=ip).exists():
              new_id = pk
              new = Vacancy.objects.get(pk=new_id)
              new.views.add(IpModel.objects.get(ip=ip))

          else:
              IpModel.objects.create(ip=ip)
              new_id = request.GET.get('pk')
              new = Vacancy.objects.get(pk=new_id)
              new.views.add(IpModel.objects.get(ip=ip))
          new = DetailVacancySerializer(new)

          return Response(new.data)