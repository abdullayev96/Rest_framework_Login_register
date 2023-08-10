from django.urls import path
from .views import *


urlpatterns  = [
          path('list/', ListServiceApi.as_view()),
          path('list/<int:pk>/',DetailServiceApi.as_view())
]