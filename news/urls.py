from django.urls import path, include
from .views import *

# from rest_framework.routers import DefaultRouter
#
#
# router = DefaultRouter()
# router.register('yangi',  Yangilik_ViewSet, basename='yangi')
# router.register('avto', Avtobus_year_ViewSet, basename='avto')
# router.register('avtoback', Avtobus_back_ViewSet, basename='avtoback')
#
#
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]


urlpatterns = [
    path('new/', NewsApi.as_view()),
    path('new/<int:pk>/', NewsDetail.as_view()),
    path('baby/', NewsBabyApi.as_view()),

]

