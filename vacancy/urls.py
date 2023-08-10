from django.urls import path
from .views import *


urlpatterns  = [
          path('vac/', VacancyListApi.as_view()),
          path('vac/<int:pk>/', VacancyDetail.as_view())
]