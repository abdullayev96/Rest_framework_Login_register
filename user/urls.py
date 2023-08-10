from django.urls import path
from .views import *

urlpatterns  = [
          path('send/',UserSendApi.as_view()),
          path('send/<int:pk>/',UserDetailApi.as_view()),
          path('answer/', AnswerApi.as_view()),
]