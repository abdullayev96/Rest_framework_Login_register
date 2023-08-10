from django.urls import path
from .views import *


urlpatterns  = [
          path('avto/', AvtobusApi.as_view()),
          path('avto/<int:pk>/', AvtobusDetail.as_view()),


          path('avtoback/', AvtobusBackApi.as_view()),
          path('avtodata/', AvtoDataApi.as_view()),

          path('order/', BusOrderApi.as_view()),
          path('post/', BusOrderPostApi.as_view()),

          path('card/', BusCardApi.as_view()),


]