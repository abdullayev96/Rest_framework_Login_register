from django.urls import path
from .views import InformationApi

urlpatterns  = [
          path('info/', InformationApi.as_view())
]