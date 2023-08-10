from  django.urls import path
from .views import *

urlpatterns  = [
          path('pat/',PartnersApi.as_view()),

]