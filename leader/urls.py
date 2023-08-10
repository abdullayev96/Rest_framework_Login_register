from django.urls import path
from .views import *


urlpatterns  = [
          path('lead/', LeaderApi.as_view()),
          path('lead/<int:pk>/', LeaderDetail.as_view()),

]